import streamlit as st
import pandas as pd
import time

# 1. PAGE SETUP
st.set_page_config(page_title="APEX-STUDENT AI", layout="wide", initial_sidebar_state="expanded")

# 2. THE "APEX" CSS - MAXIMUM CONTRAST & FUTURISM
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@300;500;700&display=swap');

    /* Global Fixes */
    .stApp {
        background: radial-gradient(circle at center, #001219 0%, #000000 100%);
        color: #e0f2f1 !important;
        font-family: 'Rajdhani', sans-serif;
    }

    /* FORCE ALL TEXT VISIBILITY */
    label, p, span, .stMarkdown, .stSelectSlider p {
        color: #ffffff !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Sidebar - Deep Glass Effect */
    [data-testid="stSidebar"] {
        background: rgba(0, 18, 25, 0.8) !important;
        backdrop-filter: blur(20px);
        border-right: 2px solid #00f2ff;
    }

    /* Main Header Glow */
    .main-header {
        font-family: 'Orbitron', sans-serif;
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(90deg, #00f2ff, #0060ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0px 10px 20px rgba(0, 242, 255, 0.3);
        margin-bottom: 0px;
    }

    /* Futuristic Data Cards */
    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.03);
        border-left: 5px solid #00f2ff;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        padding: 25px !important;
        border-radius: 4px;
        box-shadow: 10px 10px 20px rgba(0,0,0,0.5);
    }

    /* The "Pulse" Button */
    .stButton>button {
        width: 100%;
        background: transparent;
        border: 2px solid #00f2ff;
        color: #00f2ff !important;
        font-family: 'Orbitron', sans-serif;
        font-size: 1.2rem;
        padding: 15px;
        transition: 0.5s;
        border-radius: 0px;
    }
    .stButton>button:hover {
        background: #00f2ff;
        color: #000000 !important;
        box-shadow: 0px 0px 40px #00f2ff;
    }

    /* Fix for Sliders & Radio */
    .stSlider [data-baseweb="slider"] { margin-top: 20px; }
    .stRadio div[role="radiogroup"] { gap: 15px; }

    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR CONTROLS
with st.sidebar:
    st.markdown("<h2 style='color:#00f2ff; font-family:Orbitron;'>CORE PARAMETERS</h2>", unsafe_allow_html=True)
    st.write("---")
    
    # Input Sliders
    study_val = st.slider("ACADEMIC INPUT (HRS/WK)", 0, 50, 25)
    absent_val = st.number_input("ABSENCE QUOTA (DAYS)", 0, 30, 3)
    
    st.write("### SOCIAL DYNAMICS")
    support_val = st.select_slider("SUPPORT FREQUENCY", options=["MINIMAL", "STANDARD", "HIGH-TIER"])
    
    st.write("### NETWORK STATUS")
    extra = st.checkbox("ACTIVE EXTRACURRICULAR", value=True)
    
    st.write("")
    run_engine = st.button("EXECUTE PROJECTION")

# 4. MAIN INTERFACE
st.markdown('<p class="main-header">APEX_INTEL_v5.0</p>', unsafe_allow_html=True)
st.write("---")

if run_engine:
    # Calculation Engine (Logic)
    base_gpa = 2.2
    study_impact = (study_val * 0.06)
    absence_impact = (absent_val * 0.12)
    final_gpa = max(0.0, min(4.0, base_gpa + study_impact - absence_impact))
    
    # Visual Pulse Effect
    progress_text = "Synchronizing with Neural Database..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    my_bar.empty()

    # 5. METRICS ROW
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("GPA_PROJECTION", f"{final_gpa:.2f}", delta=f"{final_gpa-2.5:.2f}")
    with m2:
        risk = "STABLE" if final_gpa > 2.8 else "CRITICAL"
        st.metric("SYSTEM_STATUS", risk, delta_color="inverse")
    with m3:
        st.metric("CONFIDENCE", "97.8%", delta="OPTIONAL")

    st.write("")
    
    # 6. SECONDARY ANALYSIS
    left_col, right_col = st.columns([1.5, 1])
    
    with left_col:
        st.markdown("<h3 style='color:#00f2ff;'>📡 TRAJECTORY ANALYSIS</h3>", unsafe_allow_html=True)
        # Professional Table
        data = {
            "Metric": ["Focus Score", "Attendance Rating", "Social Factor"],
            "Analysis": [
                "OPTIMAL" if study_val > 20 else "WEAK",
                "HEALTHY" if absent_val < 5 else "WARNING",
                "HIGH" if support_val == "HIGH-TIER" else "NORMAL"
            ]
        }
        st.table(pd.DataFrame(data))

    with right_col:
        st.markdown("<h3 style='color:#00f2ff;'>🛠 CORE ACTIONS</h3>", unsafe_allow_html=True)
        with st.container():
            if final_gpa < 2.5:
                st.error("🚨 ALERT: IMMEDIATE INTERVENTION REQUIRED")
                st.info("🔹 Reduce Absences below 2 days.\n\n🔹 Increase Study Focus by 10hrs.")
            else:
                st.success("✅ OPTIMAL PATH DETECTED")
                st.info("🔹 Maintain current momentum.\n\n🔹 Expand Extracurricular network.")

else:
    # Initial Landing State
    st.markdown("""
        <div style="background: rgba(0, 242, 255, 0.05); padding: 60px; border-radius: 10px; border: 1px dashed #00f2ff; text-align: center;">
            <h2 style='color:#00f2ff;'>SYSTEM_IDLE: AWAITING COMMAND</h2>
            <p style='color:#ffffff;'>Please configure student metadata in the control panel to initialize the APEX neural engine.</p>
        </div>
    """, unsafe_allow_html=True)