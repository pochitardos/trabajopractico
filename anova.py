import pandas as pd
from scipy.stats import f_oneway
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

df = pd.read_csv('bmi.csv')

alfa = 0.05

# ANOVA 1 factor (Edad vs. Altura)
df_subset = df[df['país'] == 'argentina']
resultado_anova = f_oneway(df_subset[df_subset['edad'] == 'adolescente']['altura (cm)'], df_subset[df_subset['edad'] == 'adulto']['altura (cm)'])

print("\nANOVA de un factor (Edad vs. Altura):")
print(f"Estadístico F: {resultado_anova.statistic:.2f}")
print(f"Valor p: {resultado_anova.pvalue:.4f}")

if resultado_anova.pvalue < alfa:
    print("\n Se rechaza la hipótesis nula. Existe una diferencia significativa en la altura entre adolescentes y adultos en Argentina.")
else:
    print("\n No se puede rechazar la hipótesis nula. No hay suficiente evidencia para afirmar una diferencia significativa en la altura entre adolescentes y adultos en Argentina.")

# ANOVA dos factores (edad y país vs peso)

df.rename(columns={'peso (kg)': 'peso_kg'}, inplace=True)

modelo_anova = ols('peso_kg ~ C(edad) * C(país)', data=df).fit()
tabla_anova = anova_lm(modelo_anova, typ=2)

print("\nA NOVA de dos factores (Edad y País vs. Peso):")
print(tabla_anova)

if any(tabla_anova['PR(>F)'] < alfa):
    print("\n Se rechaza la hipótesis nula para al menos uno de los factores o su interacción. Existen diferencias significativas entre grupos.")
else:
    print("\n No se puede rechazar la hipótesis nula. No hay suficiente evidencia para afirmar diferencias significativas entre grupos.")
