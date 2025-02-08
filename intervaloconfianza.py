import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv('bmi.csv')

df_S1 = df[(df['edad'] == 'adolescente') & (df['país'] == 'usa')]
df_S2 = df[(df['edad'] == 'adulto') & (df['país'] == 'argentina')]

np.random.seed(42) # utilizo esta funcion para que las muestras aleatorias de S1 y S2 sean consistentes y reproducibles

muestra_S1 = df_S1['altura (cm)'].sample(n=100, random_state=42)
muestra_S2 = df_S2['altura (cm)'].sample(n=80, random_state=42)

# Calculo intervalo de confianza para la media de S1 (nivel 95%)
media_S1 = muestra_S1.mean()
desvio_S1 = muestra_S1.std()
n_S1 = len(muestra_S1)
sem_S1 = desvio_S1 / np.sqrt(n_S1)
conf_int_S1 = stats.norm.interval(0.95, loc=media_S1, scale=sem_S1)

# Calculo intervalo de confianza para la media de S2 (nivel 95%)
media_S2 = muestra_S2.mean()
desvio_S2 = muestra_S2.std()
n_S2 = len(muestra_S2)
sem_S2 = desvio_S2 / np.sqrt(n_S2)
conf_int_S2 = stats.norm.interval(0.95, loc=media_S2, scale=sem_S2)

# Calculo intervalo de confianza para la diferencia de medias (nivel 95%)
dif_medias = media_S1 - media_S2
sem_dif_medias = np.sqrt(sem_S1**2 + sem_S2**2)
conf_int_dif_medias = stats.norm.interval(0.95, loc=dif_medias, scale=sem_dif_medias)

# Calculo de intervalos de confianza para la varianza de S1 (nivel 80%)
var_S1 = np.var(muestra_S1, ddof=1)
chi2_inf_S1, chi2_sup_S1 = stats.chi2.interval(0.80, df=n_S1-1)
conf_int_var_S1 = ((n_S1-1) * var_S1 / chi2_sup_S1, (n_S1-1) * var_S1 / chi2_inf_S1)

# Calculo de intervalos de confianza para la varianza de S2 (nivel 80%)
var_S2 = np.var(muestra_S2, ddof=1)
chi2_inf_S2, chi2_sup_S2 = stats.chi2.interval(0.80, df=n_S2-1)
conf_int_var_S2 = ((n_S2-1) * var_S2 / chi2_sup_S2, (n_S2-1) * var_S2 / chi2_inf_S2)

print("\nValidación con los parámetros estimados:")

print(f"Media de S1: {media_S1:.2f}, ¿dentro del intervalo? {conf_int_S1[0] <= media_S1 <= conf_int_S1[1]}")
print(f"Media de S2: {media_S2:.2f}, ¿dentro del intervalo? {conf_int_S2[0] <= media_S2 <= conf_int_S2[1]}")
print(f"Diferencia de medias (S1 - S2): {dif_medias:.2f}, ¿dentro del intervalo? {conf_int_dif_medias[0] <= dif_medias <= conf_int_dif_medias[1]}")

var_S1 = np.var(muestra_S1)
var_S2 = np.var(muestra_S2)
print(f"Varianza de S1: {var_S1:.2f}, ¿dentro del intervalo? {conf_int_var_S1[0] <= var_S1 <= conf_int_var_S1[1]}")
print(f"Varianza de S2: {var_S2:.2f}, ¿dentro del intervalo? {conf_int_var_S2[0] <= var_S2 <= conf_int_var_S2[1]}")

# Curva de operacion

alpha = 0.05
sem_S1 = desvio_S1 / np.sqrt(n_S1)

z_critico = stats.norm.ppf(1 - alpha/2)

margen_error = z_critico * sem_S1

region_rechazo_superior = media_S1 + margen_error
region_rechazo_inferior = media_S1 - margen_error

medias = np.linspace(media_S1 - 3 * sem_S1, media_S1 + 3 * sem_S1, 100)

curva_operacion = np.array([stats.norm.cdf(z_critico - np.abs((media - media_S1) / sem_S1)) + (1 - stats.norm.cdf(z_critico + np.abs((media - media_S1) / sem_S1))) for media in medias])

curva_operacion = (curva_operacion - curva_operacion.min()) / (curva_operacion.max() - curva_operacion.min())

plt.figure(figsize=(10, 6))
plt.plot(medias, curva_operacion, color='black', lw=2, label='Curva de operación')
plt.axvline(x=media_S1, color='maroon', linestyle='--', lw=2, label='Media muestral de S1')
plt.fill_between(medias, 0, curva_operacion, where=(medias >= region_rechazo_superior) | (medias <= region_rechazo_inferior), color='gray', alpha=0.2, label='Región de rechazo')
plt.title('Curva de operación del test de hipótesis para la media de S1')
plt.xlabel('Media')
plt.ylabel('Probabilidad de rechazo de H0')
plt.legend()
plt.grid(True)
plt.show()