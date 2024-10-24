import streamlit as st
import pickle
import numpy as np
import pandas as pd
from datetime import datetime

# Import the trained model
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

# Set page config
st.set_page_config(
    page_title="Laptop Price Predictor",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS with modern styling
st.markdown("""
    <style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
    
    * {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Main container styling */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #e4e8f1 100%);
        padding: 2rem;
    }
    
    /* Hero section */
    .hero-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        text-align: center;
        color: white;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        background: linear-gradient(to right, #fff, #e0e0e0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
        opacity: 0.9;
        max-width: 600px;
        margin: 0 auto;
    }
    
    /* Card styling */
    .card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
        border: 1px solid rgba(255,255,255,0.2);
        backdrop-filter: blur(10px);
    }
    
    /* Section headers */
    .section-title {
        font-size: 1.5rem;
        color: #4a5568;
        margin-bottom: 1.5rem;
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Input styling */
    .stSelectbox > div > div > div {
        background-color: #f7fafc;
        border: 2px solid #e2e8f0;
        border-radius: 10px;
        padding: 0.5rem;
        transition: all 0.3s ease;
    }
    
    .stSelectbox > div > div > div:hover {
        border-color: #667eea;
    }
    
    /* Slider styling */
    .stSlider > div > div > div {
        background-color: #667eea;
    }
    
    /* Button styling */
    .predict-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1rem 2rem;
        border-radius: 10px;
        border: none;
        font-weight: 600;
        font-size: 1.1rem;
        margin: 2rem auto;
        display: block;
        min-width: 200px;
        cursor: pointer;
        transition: transform 0.3s ease;
    }
    
    .predict-button:hover {
        transform: translateY(-2px);
    }
    
    /* Result card styling */
    .result-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 2rem 0;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        animation: slideUp 0.5s ease;
    }
    
    @keyframes slideUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Feature badge */
    .feature-badge {
        background: rgba(102, 126, 234, 0.1);
        color: #667eea;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.9rem;
        margin-bottom: 1rem;
        display: inline-block;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div class="hero-container">
        <div class="hero-title">🚀 Laptop Price Predictor</div>
        <p class="hero-subtitle">
            Get accurate price estimates for your dream laptop using advanced machine learning
        </p>
    </div>
""", unsafe_allow_html=True)

# Main content
left_col, right_col = st.columns([1, 1])

with left_col:
    st.markdown("""
        <div class="card">
            <span class="feature-badge">Basic Specifications</span>
            <h3 class="section-title">📱 Core Features</h3>
        </div>
    """, unsafe_allow_html=True)
    
    company = st.selectbox('Brand', df['Company'].unique())
    type = st.selectbox('Type', df['TypeName'].unique())
    ram = st.selectbox('RAM (GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
    weight = st.number_input('Weight (kg)', min_value=0.0, max_value=5.0, value=1.5, step=0.1)
    
    st.markdown("""
        <div class="card">
            <span class="feature-badge">Performance</span>
            <h3 class="section-title">⚡ Hardware Specifications</h3>
        </div>
    """, unsafe_allow_html=True)
    
    cpu = st.selectbox('CPU Brand', df['Cpu brand'].unique())
    gpu = st.selectbox('GPU Brand', df['Gpu brand'].unique())
    
    storage_col1, storage_col2 = st.columns(2)
    with storage_col1:
        hdd = st.selectbox('HDD Storage (GB)', [0, 128, 256, 512, 1024, 2048])
    with storage_col2:
        ssd = st.selectbox('SSD Storage (GB)', [0, 8, 128, 256, 512, 1024])

with right_col:
    st.markdown("""
        <div class="card">
            <span class="feature-badge">Display</span>
            <h3 class="section-title">🖥️ Screen Specifications</h3>
        </div>
    """, unsafe_allow_html=True)
    
    touch_col, ips_col = st.columns(2)
    with touch_col:
        touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
    with ips_col:
        ips = st.selectbox('IPS Display', ['No', 'Yes'])
    
    screen_size = st.slider('Screen Size (inches)', 10.0, 18.0, 13.0, step=0.1)
    resolution = st.selectbox('Screen Resolution', 
        ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', 
         '2880x1800', '2560x1600', '2560x1440', '2304x1440'])
    
    st.markdown("""
        <div class="card">
            <span class="feature-badge">Software</span>
            <h3 class="section-title">💻 Operating System</h3>
        </div>
    """, unsafe_allow_html=True)
    
    os = st.selectbox('Operating System', df['os'].unique())

# Processing inputs
touchscreen = 1 if touchscreen == 'Yes' else 0
ips = 1 if ips == 'Yes' else 0
X_res = int(resolution.split('x')[0])
Y_res = int(resolution.split('x')[1])
ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size

# Create query DataFrame
query = pd.DataFrame({
    'Company': [company], 'TypeName': [type], 'Ram': [ram],
    'Weight': [weight], 'Touchscreen': [touchscreen], 'Ips': [ips],
    'ScreenResolution': [resolution], 'ppi': [ppi], 'Cpu brand': [cpu],
    'HDD': [hdd], 'SSD': [ssd], 'Gpu brand': [gpu], 'os': [os]
})

# Predict button
st.markdown('<button class="predict-button stButton" id="predict">Predict Price</button>', unsafe_allow_html=True)
predict_clicked = st.button('Predict Price', key='predict_price')

# Show prediction
if predict_clicked:
    with st.spinner('Analyzing specifications...'):
        predicted_price = pipe.predict(query)
        formatted_price = f"₹{int(np.exp(predicted_price[0])):,}"
        
        st.markdown(f"""
            <div class="result-card">
                <h4 style='font-size: 1.2rem; opacity: 0.9;'>Estimated Price</h4>
                <h2 style='font-size: 3rem; margin: 1rem 0;'>{formatted_price}</h2>
                <p style='opacity: 0.8;'>Prediction based on current market trends</p>
                <p style='font-size: 0.9rem; opacity: 0.7;'>
                    Last updated: {datetime.now().strftime('%B %d, %Y at %H:%M')}
                </p>
            </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style='text-align: center; padding: 2rem; opacity: 0.7;'>
        Powered by Machine Learning | Made with ❤️ using Streamlit
    </div>
""", unsafe_allow_html=True)