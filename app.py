import streamlit as st
import pandas as pd
import base64
import re
from datetime import datetime
from urllib.parse import quote

# Configuración de la página MEJORADA
st.set_page_config(
    page_title="Ramas Seguros Generales",
    page_icon="fotos/favicon.ico",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS personalizado MEJORADO para Safari y móviles
st.markdown("""
<style>
    /* Importar fuente profesional */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&display=swap');
    
    /* RESET PARA SAFARI */
    * {
        -webkit-box-sizing: border-box;
        -moz-box-sizing: border-box;
        box-sizing: border-box;
        font-family: 'Montserrat', sans-serif !important;
    }
    
    /* Fondo amarillo tenue para TODA la página */
    html, body, [data-testid="stAppViewContainer"], .main, .stApp {
        background: linear-gradient(180deg, #FFFEF7 0%, #FFF9E6 100%) !important;
        font-family: 'Montserrat', sans-serif;
    }
    
    /* SOLUCIÓN PARA PLACEHOLDERS EN SAFARI */
    .stTextInput input::placeholder {
        color: #666 !important;
        opacity: 1 !important;
        font-size: 16px !important;
    }
    
    /* FORZAR DISPLAY DE LABELS EN SAFARI */
    .stTextInput label, .stRadio label {
        display: block !important;
        visibility: visible !important;
        font-weight: 600 !important;
        color: #262730 !important;
        margin-bottom: 8px !important;
    }
    
    /* MEJORAS ESPECÍFICAS PARA SAFARI MOBILE */
    @media not all and (min-resolution:.001dpcm) { 
        @supports (-webkit-appearance:none) {
            .stTextInput input, .stTextInput input::placeholder {
                font-size: 16px !important;
                line-height: 1.5 !important;
            }
            
            .stRadio > div {
                background-color: rgba(255, 254, 247, 0.8) !important;
                padding: 1rem !important;
                border-radius: 10px !important;
                border: 1px solid #FFD700 !important;
            }
        }
    }
    
    /* RESPONSIVE PARA MÓVILES */
    @media only screen and (max-width: 768px) {
        .main .block-container {
            padding: 1rem !important;
        }
        
        .header-box {
            padding: 1.5rem 1rem !important;
        }
        
        .header-box h1 {
            font-size: 2rem !important;
        }
        
        .header-box p {
            font-size: 1.1rem !important;
        }
    }
    
    /* Estilo de botones */
    .stButton>button { 
        border-radius: 10px; 
        font-size: 1.1rem;
        font-weight: 600;
        min-height: 3rem;
    }
    
    /* Botón WhatsApp verde */
    .stButton>button[kind="primary"] {
        background-color: #25D366 !important;
        border-color: #25D366 !important;
        color: white !important;
    }
    .stButton>button[kind="primary"]:hover {
        background-color: #128C7E !important;
        border-color: #128C7E !important;
    }
    
    /* Header amarillo */
    .header-box {
        background: linear-gradient(135deg, #FFD700, #FFC107);
        color: black;
        padding: 2.5rem 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    
    /* Títulos y textos */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Montserrat', sans-serif !important;
        font-weight: 700 !important;
    }
    
    /* Inputs mejorados */
    .stTextInput > div > div > input {
        background-color: #FFFEF7 !important;
        border: 1px solid #FFD700 !important;
        border-radius: 8px !important;
        padding: 0.75rem !important;
        font-size: 16px !important;
    }
    
    /* Contenedor de formulario */
    .stForm {
        background-color: rgba(255, 254, 247, 0.8) !important;
        border: 1px solid rgba(255, 215, 0, 0.3) !important;
        border-radius: 15px !important;
        padding: 1.5rem !important;
        margin-bottom: 1.5rem !important;
    }
    
    /* Cajas de radio buttons */
    .stRadio > div {
        background-color: rgba(255, 254, 247, 0.4) !important;
        padding: 1rem !important;
        border-radius: 10px !important;
    }
    
    /* Contenedor principal */
    .block-container {
        background-color: transparent !important;
    }
    
    /* OCULTAR MENSAJES DE STREAMLIT EN INGLÉS */
    /* Ocultar "Press Enter to submit form" */
    [data-testid="stFormSubmitButton"] + div,
    .stForm [data-testid="InputInstructions"],
    [data-testid="InputInstructions"] {
        display: none !important;
        visibility: hidden !important;
    }
    
    /* Ocultar contador de caracteres en inglés */
    .stTextInput [data-testid="stCaptionContainer"] {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

# Función para cargar imagen
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception:
        return ""

logo_base64 = get_base64_image("fotos/logo.jpg")
logo_html = f'<img src="data:image/jpeg;base64,{logo_base64}" style="max-width: 150px; height: auto; margin-bottom: 15px;">' if logo_base64 else ""

# HEADER PROFESIONAL
st.markdown(f"""
<div class='header-box'>
    {logo_html}
    <h1 style='margin: 0; font-size: 2.8rem;'>Ramas Seguros Generales</h1>
    <p style='margin: 0; font-size: 1.4rem; margin-top: 0.5rem;'>Más de 11 años protegiendo tu tranquilidad</p>
</div>
""", unsafe_allow_html=True)

# TEXTO DE BIENVENIDA
st.markdown("""
<h2 style='text-align: center; color: #0066cc; margin-bottom: 1rem;'>
    ¡Cotizá tu Seguro General!
</h2>
<p style='text-align: center; font-size: 1.2rem; color: #555;'>
    Completá el formulario o contactanos por WhatsApp directamente
</p>
""", unsafe_allow_html=True)

# Inicializar estado del formulario
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False

# Funciones de validación
def validar_patente(patente):
    """Valida formato de patente argentina (vieja y nueva)"""
    # Formato viejo: ABC123 o formato nuevo: AB123CD
    patron_viejo = r'^[A-Z]{3}\d{3}$'
    patron_nuevo = r'^[A-Z]{2}\d{3}[A-Z]{2}$'
    return bool(re.match(patron_viejo, patente) or re.match(patron_nuevo, patente))

def validar_codigo_postal(cp):
    """Valida que sea un código postal argentino válido"""
    return cp.isdigit() and 1000 <= int(cp) <= 9999

if not st.session_state.form_submitted:
    # FORMULARIO PRINCIPAL MEJORADO
    with st.form("formulario_cotizacion"):
        st.markdown("### 📝 Información del Vehículo")
        
        col1, col2 = st.columns(2)
        with col1:
            patente = st.text_input(
                "**Patente** *", 
                placeholder="Ingresá la patente (Ej: AB123CD)",
                max_chars=7,
                help="Formato válido: ABC123 o AB123CD"
            ).upper()
        with col2:
            codigo_postal = st.text_input(
                "**Código Postal** *", 
                placeholder="Ingresá el código postal (Ej: 1425)",
                max_chars=4,
                help="Código postal de 4 dígitos (1000-9999)"
            )
        
        combustible = st.radio(
            "**¿Tiene instalado algún otro tipo de combustible?**",
            ["Nafta", "GNC", "Gasoil", "Eléctrico"],
            horizontal=False
        )
        
        submitted = st.form_submit_button("🚀 GENERAR COTIZACIÓN POR WHATSAPP", type="primary", use_container_width=True)
        
        if submitted:
            errores = []
            
            # Validaciones
            if not patente:
                errores.append("❌ La patente es obligatoria")
            elif not validar_patente(patente):
                errores.append("❌ Formato de patente inválido (use ABC123 o AB123CD)")
            
            if not codigo_postal:
                errores.append("❌ El código postal es obligatorio")
            elif not validar_codigo_postal(codigo_postal):
                errores.append("❌ Código postal inválido (debe ser 4 dígitos entre 1000-9999)")
            
            if errores:
                for error in errores:
                    st.error(error)
            else:
                # Mostrar spinner mientras procesa
                with st.spinner('⏳ Procesando...'):
                    st.session_state.form_submitted = True
                    st.session_state.form_data = {
                        'patente': patente,
                        'codigo_postal': codigo_postal,
                        'combustible': combustible
                    }
                st.rerun()

else:
    # RECUPERAR DATOS Y MOSTRAR ÉXITO
    data = st.session_state.form_data
    
    # GUARDAR EN CSV (backup)
    nuevo_lead = {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'patente': data['patente'],
        'codigo_postal': data['codigo_postal'],
        'combustible': data['combustible']
    }
    
    try:
        df = pd.DataFrame([nuevo_lead])
        try:
            existing_df = pd.read_csv('cotizaciones_ramas.csv')
            final_df = pd.concat([existing_df, df], ignore_index=True)
        except FileNotFoundError:
            final_df = df
        final_df.to_csv('cotizaciones_ramas.csv', index=False)
    except Exception as e:
        st.warning(f"No se pudo guardar el backup: {e}")
    
    # CREAR MENSAJE WHATSAPP CON TODOS LOS DATOS
    mensaje = f"""*COTIZACIÓN RAMAS SEGUROS*

*INFORMACIÓN DEL VEHÍCULO*
• Patente: {data['patente']}
• Código Postal: {data['codigo_postal']}
• Combustible: {data['combustible']}

_Gracias. Espero mi cotización._"""
    
    mensaje_codificado = quote(mensaje)
    TU_NUMERO_WHATSAPP = "5491136995733"
    whatsapp_url = f"https://wa.me/{TU_NUMERO_WHATSAPP}?text={mensaje_codificado}"
    
    # MOSTRAR ÉXITO Y BOTÓN WHATSAPP
    st.success("✅ **¡Datos guardados correctamente!**")
    
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, #d4edda, #c3e6cb); 
                padding: 2rem; 
                border-radius: 15px; 
                border: 2px solid #28a745; 
                text-align: center;
                margin: 1.5rem 0;'>
        <h2 style='color: #155724; margin-bottom: 1rem;'>📱 Siguiente Paso</h2>
        <p style='font-size: 1.2rem; color: #155724;'>
            <strong>Hacé clic en el botón verde de abajo para enviar tu consulta por WhatsApp</strong>
        </p>
        <p style='color: #0c5460; margin-top: 0.5rem;'>
            Se abrirá WhatsApp con todos tus datos ya cargados
        </p>
    </div>
    
    <div style='text-align: center; margin: 2rem 0;'>
        <a href="{whatsapp_url}" target="_blank" style='text-decoration: none;'>
            <button style='
                background-color: #25D366;
                color: white;
                border: none;
                padding: 18px 40px;
                border-radius: 12px;
                font-size: 1.3rem;
                font-weight: bold;
                cursor: pointer;
                box-shadow: 0 4px 12px rgba(37, 211, 102, 0.4);
                transition: all 0.3s ease;
                width: 100%;
                max-width: 500px;
            ' onmouseover='this.style.backgroundColor="#128C7E"; this.style.boxShadow="0 6px 16px rgba(18, 140, 126, 0.5)"' 
               onmouseout='this.style.backgroundColor="#25D366"; this.style.boxShadow="0 4px 12px rgba(37, 211, 102, 0.4)"'>
                📱 ENVIAR COTIZACIÓN A WHATSAPP
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Botón para nueva cotización
    if st.button("⬅️ Nueva Cotización", use_container_width=True):
        st.session_state.form_submitted = False
        st.rerun()

# BOTÓN WHATSAPP ALTERNATIVO
st.markdown("---")
st.markdown("### 💬 ¿Preferís hablar directo?")

mensaje_rapido = "Hola Ramas Seguros! Quiero información sobre seguros vehiculares"
whatsapp_url_rapido = f"https://wa.me/5491136995733?text={quote(mensaje_rapido)}"

st.markdown(f"""
<a href="{whatsapp_url_rapido}" target="_blank">
    <button style='
        background-color: #0088cc;
        color: white;
        border: none;
        padding: 14px 28px;
        border-radius: 10px;
        font-size: 1.1rem;
        cursor: pointer;
        width: 100%;
        margin: 10px 0;
        font-weight: bold;
    '>
        💬 CONTACTAR POR WHATSAPP
    </button>
</a>
""", unsafe_allow_html=True)

# FOOTER
st.markdown("---")

# Cargar favicon para el footer
favicon_base64 = get_base64_image("fotos/favicon.ico")
favicon_html = f'<img src="data:image/x-icon;base64,{favicon_base64}" style="width: 24px; height: 24px; vertical-align: middle; margin-right: 8px;">' if favicon_base64 else "🏢"

st.markdown(f"""
<div style='text-align: center; color: #666; padding: 1.5rem;'>
    <p style='font-size: 1.1rem; margin: 0;'>{favicon_html} <strong>Ramas Seguros Generales</strong> - Protegiendo lo que más importa</p>
    <p style='font-size: 0.9rem; margin: 0.5rem 0 0 0;'>Tu tranquilidad es nuestra prioridad</p>
</div>
""", unsafe_allow_html=True)