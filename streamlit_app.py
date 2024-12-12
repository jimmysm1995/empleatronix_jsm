import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.title("EMPLEATRONIX")
st.write("Todos los datos sobre los empleados en una aplicación.")

df = pd.read_csv("data/employees.csv")
st.dataframe(df)
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    color = st.color_picker("Elige un color para las barras", "#3475B3")

with col2:
    mostrar_nombre = st.toggle("Mostrar el nombre", value=True)

with col3:
    mostrar_sueldo = st.toggle("Mostrar sueldo en la barra")

# Crear la gráfica de barras horizontal
fig, ax = plt.subplots()
sns.barplot(x="salary", y="full name", data=df, ax=ax, color=color)

# Ocultar las etiquetas del eje x
ax.set_xlabel("")
ax.set_ylabel("")

# Mostrar los nombres y sueldos en las barras si están seleccionados
if not mostrar_nombre:
    ax.set_yticklabels([])
if mostrar_sueldo:
    for i in ax.containers:
        ax.bar_label(i, label_type='edge', labels=[f"{salary}€" for salary in df["salary"]] if mostrar_sueldo else None)

st.pyplot(fig)
st.write("© José Sánchez Martínez - CPIFP Alan Turing")