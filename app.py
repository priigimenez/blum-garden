import streamlit as st  # Streamlit para la app web
import pandas as pd     # Pandas para leer/guardar notas
from datetime import date  # Para registrar la fecha de cada nota

# Configurar la página (título y layout centrado)
st.set_page_config(page_title="Blum Garden 🌿", layout="centered")

# Título principal y subtítulo motivador
st.title("🌱 Diario de Aprendizaje")
st.markdown("Anotá lo que aprendiste hoy, lo que sentiste, lo que descubriste. Tu jardín crece con cada nota que plantás. 🌼")

# Función para cargar las notas anteriores desde un archivo CSV
def load_notes():
    try:
        return pd.read_csv("notas.csv")  # Intenta leer el archivo si existe
    except FileNotFoundError:
        return pd.DataFrame(columns=["fecha", "nota"])  # Si no existe, crea uno vacío

notes_df = load_notes()  # Guardamos las notas cargadas en una variable

# Formulario para escribir una nueva nota
with st.form("form_nota"):
    nota = st.text_area("✍️ Escribí tu aprendizaje o reflexión de hoy", height=150)  # Caja para escribir
    submitted = st.form_submit_button("Guardar")  # Botón de guardar

    # Si se envió el formulario y hay texto, guardamos la nota
    if submitted and nota.strip() != "":
        nueva_nota = pd.DataFrame([[str(date.today()), nota]], columns=["fecha", "nota"])
        notes_df = pd.concat([nueva_nota, notes_df], ignore_index=True)  # Insertamos al principio
        notes_df.to_csv("notas.csv", index=False)  # Guardamos todas las notas
        st.success("🌷 Nota guardada en tu jardín digital")

# Línea divisoria visual
st.divider()

# Mostrar las notas guardadas en formato de tarjetas visuales
st.subheader("🌼 Tus notas")
if notes_df.empty:
    st.info("Todavía no agregaste ninguna nota.")
else:
    for i, row in notes_df.iterrows():
        # Mostrar cada nota como una tarjetita linda
        st.markdown(f"""
        <div style="background-color:#f4f4f4; padding:15px; margin-bottom:10px; border-radius:10px">
            <small>{row['fecha']}</small>
            <p>{row['nota']}</p>
        </div>
        """, unsafe_allow_html=True)
