
import pandas as pd
import matplotlib.pyplot as plt

# Johan Paulo Aros Reveles NC 0016

print("ANALISIS EXPLORATORIO DE DATOS EDA")
print("Salud y Medicina - Equipos de Ultrasonido")
print("Desarrollado por Johan Paulo Aros")

# 1. Crear diccionario con 10 listas y 6 elementos
equipos_ultrasonido = {
    'id_equipo': [301, 302, 303, 304, 305, 306],
    'marca': ['GE', 'Philips', 'Siemens', 'GE', 'Canon', 'Philips'],
    'modelo': ['Voluson E8', 'EPIQ 7', 'Acuson S2000', 'Logiq E9', 'Aplio 500', 'Affiniti 70'],
    'ano_fabricacion': [2018, 2020, 2019, 2021, 2017, 2022],
    'ubicacion': ['Ginecologia', 'Cardiologia', 'Radiologia', 'Radiologia', 'Ginecologia', 'Cardiologia'],
    'estado': ['Operativo', 'Operativo', 'Mantenimiento', 'Operativo', 'Operativo', 'Operativo'],
    'horas_uso_total': [4500, 2100, 3800, 1200, 5600, 800],
    'ultimo_mantenimiento': ['2023-10', '2023-11', '2023-12', '2024-01', '2023-09', '2024-01'],
    'costo_adquisicion': [850000, 920000, 780000, 950000, 700000, 880000],
    'tecnico_asignado': ['Juan P.', 'Maria L.', 'Carlos R.', 'Juan P.', 'Ana S.', 'Maria L.']
}

# 2. Convertir diccionario en DataFrame
df = pd.DataFrame(equipos_ultrasonido)

print("\n--- TABLA ORIGINAL DE EQUIPOS ---")
print(df)

# 3. Guardar información en CSV
print("\n--- CREAR ARCHIVO CSV ---")
df.to_csv('equipos_ultrasonido_0016.csv',
          index=False, encoding='utf-8-sig')
print("Archivo CSV creado correctamente")

# 4. Leer nuevamente los datos desde CSV
print("\n--- DATOS LEIDOS DESDE CSV ---")
df = pd.read_csv('equipos_ultrasonido_0016.csv')
print(df)

# 5. Primeros y últimos registros
print("\n1. PRIMEROS REGISTROS (HEAD):")
print(df.head(3))

print("\n2. ULTIMOS REGISTROS (TAIL):")
print(df.tail(2))

# 6. Dimensiones y estructura
print("\n3. DIMENSIONES:")
print(df.shape)

print("\n4. NOMBRES DE COLUMNAS:")
print(df.columns)

print("\n5. TIPOS DE DATOS:")
print(df.dtypes)

print("\n6. INFORMACION GENERAL:")
df.info()

# 7. Estadísticas y limpieza
print("\n7. ESTADISTICAS DESCRIPTIVAS:")
print(df.describe())

print("\n8. VALORES FALTANTES:")
print(df.isnull().sum())

print("\n9. REGISTROS DUPLICADOS:")
print(df.duplicated().sum())

print("\n10. VALORES UNICOS:")
print(df.nunique())

print("\nMARCAS UNICAS:")
print(df['marca'].unique())

# 8. Análisis específico
print("\n11. EQUIPOS POR MARCA:")
print(df['marca'].value_counts())

print("\n12. PROMEDIO DEL COSTO DE ADQUISICION:")
print(df['costo_adquisicion'].mean())

print("\n13. COSTO MAXIMO:")
print(df['costo_adquisicion'].max())

print("\n14. COSTO MINIMO:")
print(df['costo_adquisicion'].min())

# 9. Ordenamiento, filtrado y agrupación
print("\n15. EQUIPOS ORDENADOS POR COSTO:")
print(df.sort_values(by='costo_adquisicion', ascending=False))

print("\n16. EQUIPOS CON COSTO MAYOR A 850000:")
filtro = df[df['costo_adquisicion'] > 850000]
print(filtro)

print("\n17. RESUMEN POR MARCA:")
resumen = df.groupby('marca').agg(
    cantidad_equipos=('id_equipo', 'count'),
    costo_promedio=('costo_adquisicion', 'mean'),
    horas_promedio=('horas_uso_total', 'mean')
)
print(resumen)

# 10. Gráfica de barras: equipos por marca
conteo = df['marca'].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(conteo.index, conteo.values, color='skyblue')
plt.title('Equipos de ultrasonido por marca')
plt.xlabel('Marca')
plt.ylabel('Cantidad de equipos')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 11. Gráfica de costos por equipo
plt.figure(figsize=(9, 5))
plt.bar(df['modelo'], df['costo_adquisicion'], color='lightgreen')
plt.title('Costo de adquisicion por equipo NC 0016')
plt.xlabel('Modelo')
plt.ylabel('Costo en pesos')
plt.xticks(rotation=30)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 12. Histograma: horas de uso
plt.figure(figsize=(8, 5))
plt.hist(df['horas_uso_total'], bins=5,
         color='orange', edgecolor='black')
plt.title('Distribucion de horas de uso NC 0016')
plt.xlabel('Horas de uso')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 13. Gráfica de dispersión: año vs costo
plt.figure(figsize=(8, 5))
plt.scatter(df['ano_fabricacion'],
            df['costo_adquisicion'],
            color='red', s=100)
plt.title('Año de fabricacion vs costo NC 0016')
plt.xlabel('Año de fabricacion')
plt.ylabel('Costo de adquisicion')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 14. Diagrama de caja: costos
plt.figure(figsize=(7, 5))
plt.boxplot(df['costo_adquisicion'],
            patch_artist=True,
            boxprops=dict(facecolor='lightblue'))
plt.title('Distribucion de costos NC 0016')
plt.ylabel('Costo de adquisicion')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 15. Matriz de correlación
correlacion = df.corr(numeric_only=True)

print("\n--- MATRIZ DE CORRELACION ---")
print(correlacion)

plt.figure(figsize=(9, 6))
plt.imshow(correlacion, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(correlacion.columns)),
           correlacion.columns, rotation=45)
plt.yticks(range(len(correlacion.columns)),
           correlacion.columns)
plt.title('Matriz de correlacion NC 0016')
plt.tight_layout()
plt.show()

# 16. Conclusiones
print("\n--- CONCLUSIONES DEL ANALISIS EDA ---")
print("1. Se analizaron 6 equipos de ultrasonido.")
print("2. Se identificaron 5 marcas diferentes.")
print("3. El equipo con mayor costo es Logiq E9? No, es el modelo Logiq E9.")
print("4. Se compararon las horas de uso de los equipos.")
print("5. Se analizaron costos, marcas y años de fabricacion.")
print("6. Los datos pueden utilizarse posteriormente en Machine Learning.")
