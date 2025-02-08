import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('bmi.csv')

df_adolescentes_usa = df[(df['edad'] == 'adolescente') & (df['país'] == 'usa')]
df_adolescentes_argentina = df[(df['edad'] == 'adolescente') & (df['país'] == 'argentina')]
df_adultos_usa = df[(df['edad'] == 'adulto') & (df['país'] == 'usa')]
df_adultos_argentina = df[(df['edad'] == 'adulto') & (df['país'] == 'argentina')]

media_altura_adolescentes_usa = df_adolescentes_usa['altura (cm)'].mean()
media_peso_adolescentes_usa = df_adolescentes_usa['peso (kg)'].mean()
mediana_altura_adolescentes_usa = df_adolescentes_usa['altura (cm)'].median()
mediana_peso_adolescentes_usa = df_adolescentes_usa['peso (kg)'].median()
desvio_altura_adolescentes_usa = df_adolescentes_usa['altura (cm)'].std()
desvio_peso_adolescentes_usa = df_adolescentes_usa['peso (kg)'].std()

media_altura_adolescentes_argentina = df_adolescentes_argentina['altura (cm)'].mean()
media_peso_adolescentes_argentina = df_adolescentes_argentina['peso (kg)'].mean()
mediana_altura_adolescentes_argentina = df_adolescentes_argentina['altura (cm)'].median()
mediana_peso_adolescentes_argentina = df_adolescentes_argentina['peso (kg)'].median()
desvio_altura_adolescentes_argentina = df_adolescentes_argentina['altura (cm)'].std()
desvio_peso_adolescentes_argentina = df_adolescentes_argentina['peso (kg)'].std()

media_altura_adultos_usa = df_adultos_usa['altura (cm)'].mean()
media_peso_adultos_usa = df_adultos_usa['peso (kg)'].mean()
mediana_altura_adultos_usa = df_adultos_usa['altura (cm)'].median()
mediana_peso_adultos_usa = df_adultos_usa['peso (kg)'].median()
desvio_altura_adultos_usa = df_adultos_usa['altura (cm)'].std()
desvio_peso_adultos_usa = df_adultos_usa['peso (kg)'].std()

media_altura_adultos_argentina = df_adultos_argentina['altura (cm)'].mean()
media_peso_adultos_argentina = df_adultos_argentina['peso (kg)'].mean()
mediana_altura_adultos_argentina = df_adultos_argentina['altura (cm)'].median()
mediana_peso_adultos_argentina = df_adultos_argentina['peso (kg)'].median()
desvio_altura_adultos_argentina = df_adultos_argentina['altura (cm)'].std()
desvio_peso_adultos_argentina = df_adultos_argentina['peso (kg)'].std()

plt.figure(figsize=(12, 5))

# Gráfico para adolescentes USA
plt.subplot(2, 2, 1)
sns.kdeplot(df_adolescentes_usa['altura (cm)'], shade=True, color='darkkhaki')
plt.title('Densidad de altura (Adolescentes - USA)')
plt.xlabel('Altura (cm)')
plt.ylabel('Densidad')

plt.axvline(media_altura_adolescentes_usa, color='black', linestyle='--', linewidth=2, label=f'Media: {media_altura_adolescentes_usa:.2f}')
plt.axvline(mediana_altura_adolescentes_usa, color='maroon', linestyle='-', linewidth=2, label=f'Mediana: {mediana_altura_adolescentes_usa:.2f}')
plt.text(0.05, 0.95, f'Desvío Estándar: {desvio_altura_adolescentes_usa:.2f}', transform=plt.gca().transAxes, va='top', ha='left', color='black')

plt.legend()

plt.subplot(2, 2, 2)
sns.kdeplot(df_adolescentes_usa['peso (kg)'], shade=True, color='tan')
plt.title('Densidad de peso (Adolescentes - USA)')
plt.xlabel('Peso (kg)')
plt.ylabel('Densidad')

plt.axvline(media_peso_adolescentes_usa, color='black', linestyle='--', linewidth=2, label=f'Media: {media_peso_adolescentes_usa:.2f}')
plt.axvline(mediana_peso_adolescentes_usa, color='maroon', linestyle='-', linewidth=2, label=f'Mediana: {mediana_peso_adolescentes_usa:.2f}')
plt.text(0.05, 0.95, f'Desvío Estándar: {desvio_peso_adolescentes_usa:.2f}', transform=plt.gca().transAxes, va='top', ha='left', color='black')

plt.legend()

# Gráfico para adolescentes Argentina
plt.subplot(2, 2, 3)
sns.kdeplot(df_adolescentes_argentina['altura (cm)'], shade=True, color='darkkhaki')
plt.title('Densidad de altura (Adolescentes - Argentina)')
plt.xlabel('Altura (cm)')
plt.ylabel('Densidad')

plt.axvline(media_altura_adolescentes_argentina, color='black', linestyle='--', linewidth=2, label=f'Media: {media_altura_adolescentes_argentina:.2f}')
plt.axvline(mediana_altura_adolescentes_argentina, color='maroon', linestyle='-', linewidth=2, label=f'Mediana: {mediana_altura_adolescentes_argentina:.2f}')
plt.text(0.05, 0.95, f'Desvío Estándar: {desvio_altura_adolescentes_argentina:.2f}', transform=plt.gca().transAxes, va='top', ha='left', color='black')


plt.legend()

plt.subplot(2, 2, 4)
sns.kdeplot(df_adolescentes_argentina['peso (kg)'], shade=True, color='tan')
plt.title('Densidad de peso (Adolescentes - Argentina)')
plt.xlabel('Peso (kg)')
plt.ylabel('Densidad')

plt.axvline(media_peso_adolescentes_argentina, color='black', linestyle='--', linewidth=2, label=f'Media: {media_peso_adolescentes_argentina:.2f}')
plt.axvline(mediana_peso_adolescentes_argentina, color='maroon', linestyle='-', linewidth=2, label=f'Mediana: {mediana_peso_adolescentes_argentina:.2f}')
plt.text(0.05, 0.95, f'Desvío Estándar: {desvio_peso_adolescentes_argentina:.2f}', transform=plt.gca().transAxes, va='top', ha='left', color='black')

plt.legend()

plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 5))

# Gráfico para adultos USA
plt.subplot(2, 2, 1)
sns.kdeplot(df_adultos_usa['altura (cm)'], shade=True, color='darkkhaki')
plt.title('Densidad de altura (Adultos - USA)')
plt.xlabel('Altura (cm)')
plt.ylabel('Densidad')

plt.axvline(media_altura_adultos_usa, color='black', linestyle='--', linewidth=2, label=f'Media: {media_altura_adultos_usa:.2f}')
plt.axvline(mediana_altura_adultos_usa, color='maroon', linestyle='-', linewidth=2, label=f'Mediana: {mediana_altura_adultos_usa:.2f}')
plt.text(0.05, 0.95, f'Desvío Estándar: {desvio_altura_adultos_usa:.2f}', transform=plt.gca().transAxes, va='top', ha='left', color='black')

plt.legend()

plt.subplot(2, 2, 2)
sns.kdeplot(df_adultos_usa['peso (kg)'], shade=True, color='tan')
plt.title('Densidad de peso (Adultos - USA)')
plt.xlabel('Peso (kg)')
plt.ylabel('Densidad')

plt.axvline(media_peso_adultos_usa, color='black', linestyle='--', linewidth=2, label=f'Media: {media_peso_adultos_usa:.2f}')
plt.axvline(mediana_peso_adultos_usa, color='maroon', linestyle='-', linewidth=2, label=f'Mediana: {mediana_peso_adultos_usa:.2f}')
plt.text(0.05, 0.95, f'Desvío Estándar: {desvio_peso_adultos_usa:.2f}', transform=plt.gca().transAxes, va='top', ha='left', color='black')

plt.legend()

# Gráfico para adultos Argentina
plt.subplot(2, 2, 3)
sns.kdeplot(df_adultos_argentina['altura (cm)'], shade=True, color='darkkhaki')
plt.title('Densidad de altura (Adultos - Argentina)')
plt.xlabel('Altura (cm)')
plt.ylabel('Densidad')

plt.axvline(media_altura_adultos_argentina, color='black', linestyle='--', linewidth=2, label=f'Media: {media_altura_adultos_argentina:.2f}')
plt.axvline(mediana_altura_adultos_argentina, color='maroon', linestyle='-', linewidth=2, label=f'Mediana: {mediana_altura_adultos_argentina:.2f}')
plt.text(0.05, 0.95, f'Desvío Estándar: {desvio_altura_adultos_argentina:.2f}', transform=plt.gca().transAxes, va='top', ha='left', color='black')

plt.legend()

plt.subplot(2, 2, 4)
sns.kdeplot(df_adultos_argentina['peso (kg)'], shade=True, color='tan')
plt.title('Densidad de peso (Adultos - Argentina)')
plt.xlabel('Peso (kg)')
plt.ylabel('Densidad')

plt.axvline(media_peso_adultos_argentina, color='black', linestyle='--', linewidth=2, label=f'Media: {media_peso_adultos_argentina:.2f}')
plt.axvline(mediana_peso_adultos_argentina, color='maroon', linestyle='-', linewidth=2, label=f'Mediana: {mediana_peso_adultos_argentina:.2f}')
plt.text(0.05, 0.95, f'Desvío Estándar: {desvio_peso_adultos_argentina:.2f}', transform=plt.gca().transAxes, va='top', ha='left', color='black')

plt.legend()

plt.tight_layout()
plt.show()
