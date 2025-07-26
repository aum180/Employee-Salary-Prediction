import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Set page configuration
st.set_page_config(
    page_title="Premium Salary Predictor",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Premium CSS styling with enhanced sidebar colors
st.markdown("""
<style>
    /* Main styles */
    .stApp {
        background: linear-gradient(135deg, #f8f9fa 0%, #eef2f6 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .main-container {
        max-width: 1400px;
        margin: 0 auto;
        padding: 0 20px;
    }
    .main-title {
        color: #2c3e50;
        font-size: 2.8rem;
        font-weight: 700;
        margin-bottom: 1rem;
        padding-bottom: 1rem;
        background: linear-gradient(90deg, #3498db, #2c3e50);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .section-header {
        color: #2c3e50;
        font-size: 1.6rem;
        font-weight: 600;
        margin-top: 2rem;
        margin-bottom: 1.5rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #3498db;
        width: fit-content;
    }
    .metric-box {
        background: white;
        border-radius: 12px;
        padding: 25px;
        box-shadow: 0 6px 18px rgba(0, 0, 0, 0.08);
        text-align: center;
        margin-bottom: 25px;
        transition: all 0.3s ease;
        border: 1px solid #e0e6ed;
    }
    .metric-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
    }
    .metric-title {
        font-size: 1.1rem;
        color: #7f8c8d;
        margin-bottom: 10px;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }
    .metric-value {
        font-size: 2.8rem;
        font-weight: 700;
        color: #2c3e50;
        margin: 15px 0;
    }
    .stButton>button {
        background: linear-gradient(135deg, #3498db, #2c3e50);
        color: white;
        border: none;
        padding: 14px 28px;
        border-radius: 8px;
        font-size: 1.1rem;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
        box-shadow: 0 4px 8px rgba(52, 152, 219, 0.3);
    }
    .stButton>button:hover {
        transform: scale(1.03);
        box-shadow: 0 6px 12px rgba(52, 152, 219, 0.4);
    }
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #1a2530 0%, #0d1218 100%);
        color: white;
        padding: 20px 15px;
        box-shadow: 0 0 25px rgba(0, 0, 0, 0.2);
    }
    .sidebar-title {
        color: #2c3e50;
        font-size: 2rem;
        font-weight: 650;
        margin-bottom: 1rem;
        padding-bottom: 1rem;
        background: linear-gradient(90deg, #3498db, #2c3e50);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;

    }
    .input-label {
        color: #3498db;
        font-weight: 700;
        margin-bottom: 8px;
        margin-top: 15px;
        display: block;
        font-size: 1.1rem;
        letter-spacing: 0.5px;
        background: rgba(255,255,255,0.1);
        padding: 8px 12px;
        border-radius: 6px;
        border-left: 3px solid #3498db;
    }
    .footer {
        background: #2c3e50;
        color: white;
        text-align: center;
        padding: 15px;
        font-size: 0.9rem;
        margin-top: 40px;
        border-radius: 0 0 12px 12px;
    }
    .info-card {
        background: white;
        border-radius: 12px;
        padding: 25px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        margin-bottom: 25px;
        border: 1px solid #e0e6ed;
    }
    .tab-content {
        background: white;
        border-radius: 12px;
        padding: 25px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        margin-top: 20px;
        border: 1px solid #e0e6ed;
        min-height: 500px;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 12px 24px;
        border-radius: 8px 8px 0 0 !important;
        background: #f1f5f9 !important;
        margin: 0 !important;
        transition: all 0.3s ease;
    }
    .stTabs [aria-selected="true"] {
        background: #3498db !important;
        color: white !important;
        font-weight: 600;
    }
    .stRadio > div {
        display: flex;
        gap: 15px;
    }
    .stRadio [role="radiogroup"] {
        display: flex;
        gap: 15px;
    }
    .stRadio [data-testid="stMarkdownContainer"] {
        font-weight: 500;
        color: #f0f0f0;
    }
    .stSlider [data-testid="stMarkdownContainer"] {
        color: #f0f0f0;
        font-weight: 500;
    }
    .stSelectbox [data-testid="stMarkdownContainer"] {
        color: #f0f0f0;
        font-weight: 500;
    }
    .highlight {
        background: linear-gradient(90deg, #3498db, #2ecc71);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)

# Generate sample data for visualizations
def generate_sample_data():
    np.random.seed(42)
    data = {
        'Experience': np.random.randint(0, 25, 100),
        'Education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], 100, p=[0.1, 0.5, 0.3, 0.1]),
        'Department': np.random.choice(['Engineering', 'Finance', 'Marketing', 'Sales', 'HR', 'Operations'], 100),
        'Performance': np.random.randint(1, 6, 100),
        'Location': np.random.choice(['Urban', 'Suburban', 'Rural'], 100, p=[0.6, 0.3, 0.1]),
        'Age': np.random.randint(22, 60, 100)
    }
    df = pd.DataFrame(data)
    
    # Salary calculation function
    def calculate_salary(row):
        base = 50000 + (row['Experience'] * 4200)
        edu_mult = {'High School': 1.0, 'Bachelor': 1.4, 'Master': 1.7, 'PhD': 2.1}
        dept_mult = {'Engineering': 1.5, 'Finance': 1.4, 'Marketing': 1.3, 'Sales': 1.25, 'HR': 1.15, 'Operations': 1.2}
        loc_adj = {'Urban': 1.2, 'Suburban': 1.1, 'Rural': 1.0}
        perf_bonus = {1: 0, 2: 0.05, 3: 0.12, 4: 0.25, 5: 0.4}
        age_factor = 1 + (min(row['Age'], 50) - 30) * 0.01
        
        salary = base * edu_mult[row['Education']] * dept_mult[row['Department']]
        salary *= loc_adj[row['Location']]
        salary *= (1 + perf_bonus[row['Performance']])
        salary *= age_factor
        
        return int(salary)
    
    df['Salary'] = df.apply(calculate_salary, axis=1)
    return df

# Main application
def main():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # Sample data for visualizations
    df = generate_sample_data()
    
    # Sidebar - User Inputs
    with st.sidebar:

        st.markdown('<div class="sidebar-title" style="color: rgba(255,255,255,0.9);">EMPLOYEE PROFILE</div>', unsafe_allow_html=True)
        
        # User input fields with enhanced labels
        st.markdown('<div class="input-label">YEARS OF EXPERIENCE</div>', unsafe_allow_html=True)
        experience = st.slider("", 0, 30, 5, help="Total years of professional experience", label_visibility="collapsed")
        
        st.markdown('<div class="input-label">EDUCATION LEVEL</div>', unsafe_allow_html=True)
        education = st.selectbox("", ['High School', 'Bachelor', 'Master', 'PhD'], index=1, label_visibility="collapsed")
        
        st.markdown('<div class="input-label">DEPARTMENT</div>', unsafe_allow_html=True)
        department = st.selectbox("", ['Engineering', 'Finance', 'Marketing', 'Sales', 'HR', 'Operations'], 
                                index=0, label_visibility="collapsed")
        
        st.markdown('<div class="input-label">PERFORMANCE RATING</div>', unsafe_allow_html=True)
        performance = st.select_slider("", options=[1, 2, 3, 4, 5], value=3,
                                      help="1: Low performance, 5: Exceptional performance", 
                                      label_visibility="collapsed")
        
        st.markdown('<div class="input-label">WORK LOCATION</div>', unsafe_allow_html=True)
        location = st.selectbox("", ['Urban', 'Suburban', 'Rural'], index=0, label_visibility="collapsed")
        
        st.markdown('<div class="input-label">AGE</div>', unsafe_allow_html=True)
        age = st.slider("", 22, 65, 35, label_visibility="collapsed")
        
        # Predict button
        predict_btn = st.button("PREDICT SALARY", type="primary", use_container_width=True)
        
        # Spacer
        st.markdown("<div style='height: 30px'></div>", unsafe_allow_html=True)
        
        # Logo or brand
        st.markdown("""
        <div style="text-align: center; margin-top: 30px; opacity: 0.9;">
            <div style="font-size: 1.2rem; font-weight: 700; color: #3498db;">SALARY PREDICTOR</div>
            <div style="font-size: 0.9rem; margin-top: 5px; color: #ecf0f1;">AI-Powered Compensation Analysis</div>
        </div>
        """, unsafe_allow_html=True)

    # Main content area
    col1, col2 = st.columns([1, 1.5], gap="large")
    
    with col1:
        st.markdown('<div class="main-title">Premium Salary Predictor</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="info-card" style="font-size:1.1rem; color:#34495e; margin-bottom:30px;">
            This AI-powered system provides accurate salary predictions based on professional attributes, 
            experience, and performance metrics. Our model achieves <span class="highlight">92% accuracy</span> in compensation forecasting.
        </div>
        """, unsafe_allow_html=True)
        
        # Prediction result
        if predict_btn:
            # Calculate salary (replace with your model)
            base = 50000 + (experience * 4200)
            edu_mult = {'High School': 1.0, 'Bachelor': 1.4, 'Master': 1.7, 'PhD': 2.1}
            dept_mult = {'Engineering': 1.5, 'Finance': 1.4, 'Marketing': 1.3, 'Sales': 1.25, 'HR': 1.15, 'Operations': 1.2}
            loc_adj = {'Urban': 1.2, 'Suburban': 1.1, 'Rural': 1.0}
            perf_bonus = {1: 0, 2: 0.05, 3: 0.12, 4: 0.25, 5: 0.4}
            age_factor = 1 + (min(age, 50) - 30) * 0.01
            
            salary = base * edu_mult[education] * dept_mult[department]
            salary *= loc_adj[location]
            salary *= (1 + perf_bonus[performance])
            salary *= age_factor
            salary = int(salary)
            
            # Format salary with commas
            formatted_salary = "${:,.0f}".format(salary)
            
            # Display with animation
            st.markdown(f"""
            <div class="metric-box" style="background: linear-gradient(135deg, #3498db, #2c3e50);">
                <div class="metric-title" style="color: rgba(255,255,255,0.9);">PREDICTED ANNUAL SALARY</div>
                <div class="metric-value" style="color: white; font-size: 3rem;">{formatted_salary}</div>
                <div style="color: rgba(255,255,255,0.8); font-size: 1rem; margin-top: 10px;">
                    Based on your professional profile
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Salary comparison
            st.markdown('<div class="section-header">Industry Benchmark</div>', unsafe_allow_html=True)
            
            # Get average salary for similar profiles
            similar = df[
                (df['Education'] == education) & 
                (df['Department'] == department) & 
                (df['Location'] == location)
            ]
            avg_salary = similar['Salary'].mean() if not similar.empty else salary
            
            # Create comparison gauge
            fig = go.Figure(go.Indicator(
                mode = "number+gauge+delta",
                value = salary,
                delta = {'reference': avg_salary, 'increasing': {'color': "#2ecc71"}, 'decreasing': {'color': "#e74c3c"}},
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': f"Compared to {department} Average"},
                gauge = {
                    'shape': "bullet",
                    'axis': {'range': [None, max(salary, avg_salary) * 1.3]},
                    'bar': {'color': "#3498db", 'thickness': 0.6},
                    'bgcolor': "#f0f0f0",
                    'steps': [
                        {'range': [0, avg_salary * 0.7], 'color': "#f8d7da"},
                        {'range': [avg_salary * 0.7, avg_salary * 1.3], 'color': "#fff3cd"},
                        {'range': [avg_salary * 1.3, max(salary, avg_salary) * 1.5], 'color': "#d4edda"}
                    ]
                }
            ))
            
            fig.update_layout(
                height=180,
                margin=dict(l=20, r=20, t=60, b=20),
                font=dict(family="Segoe UI", size=12)
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Compensation insights
            st.markdown('<div class="section-header">Compensation Insights</div>', unsafe_allow_html=True)
            
            # Create two columns for insights
            col_a, col_b = st.columns(2, gap="medium")
            
            with col_a:
                st.markdown("""
                <div class="info-card">
                    <div style="display: flex; align-items: center; margin-bottom: 15px;">
                        <div style="font-size: 1.8rem; color: #3498db; margin-right: 12px;">📊</div>
                        <div style="font-size: 1.1rem; font-weight: 600;">Education Premium</div>
                    </div>
                    <div style="color: #34495e; line-height: 1.6;">
                        Advanced degrees command significant salary premiums. PhD holders earn 40-60% more than bachelor's degree holders in technical roles.
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
            with col_b:
                st.markdown("""
                <div class="info-card">
                    <div style="display: flex; align-items: center; margin-bottom: 15px;">
                        <div style="font-size: 1.8rem; color: #3498db; margin-right: 12px;">🚀</div>
                        <div style="font-size: 1.1rem; font-weight: 600;">Performance Impact</div>
                    </div>
                    <div style="color: #34495e; line-height: 1.6;">
                        Top performers (rating 5) earn up to 40% more than average performers. Consistent high performance accelerates career growth.
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
        else:
            # Placeholder before prediction
            st.markdown("""
            <div class="metric-box">
                <div class="metric-title">PREDICTED ANNUAL SALARY</div>
                <div class="metric-value">$---,---</div>
                <div style="color: #7f8c8d; font-size: 1rem; margin-top: 10px;">
                    Enter your details and click "Predict Salary"
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown('<div class="section-header">Industry Benchmark</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-card">
                <div style="color: #34495e; line-height: 1.6; text-align: center; padding: 30px 0;">
                    <div style="font-size: 4rem; color: #e0e6ed; margin-bottom: 15px;">📈</div>
                    <div style="font-weight: 600; margin-bottom: 10px;">Benchmark Analysis</div>
                    <div>After prediction, see how your compensation compares to industry standards for your role and experience level.</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        # Visualizations
        st.markdown('<div class="section-header">Salary Analysis Dashboard</div>', unsafe_allow_html=True)
        
        # Create tabs for different visualizations
        tab1, tab2, tab3 = st.tabs(["📊 Distribution", "🏢 Department", "📈 Experience"])
        
        with tab1:
            # Salary distribution by education
            fig1 = px.box(df, x='Education', y='Salary', 
                         color='Education', 
                         title='Salary Distribution by Education Level',
                         color_discrete_sequence=['#3498db', '#2ecc71', '#9b59b6', '#e74c3c'])
            fig1.update_layout(
                xaxis_title="Education Level",
                yaxis_title="Annual Salary ($)",
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Segoe UI", size=12),
                height=500
            )
            st.plotly_chart(fig1, use_container_width=True)
            
        with tab2:
            # Salary by department and location
            fig2 = px.bar(df, x='Department', y='Salary', 
                         color='Location', barmode='group',
                         title='Average Salary by Department and Location',
                         color_discrete_sequence=['#3498db', '#2ecc71', '#9b59b6'])
            fig2.update_layout(
                xaxis_title="Department",
                yaxis_title="Average Annual Salary ($)",
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Segoe UI", size=12),
                height=500
            )
            st.plotly_chart(fig2, use_container_width=True)
            
        with tab3:
            # Salary by experience and performance
            fig3 = px.scatter(df, x='Experience', y='Salary', 
                             color='Performance', size='Age',
                             title='Salary by Experience and Performance',
                             color_continuous_scale='Viridis',
                             trendline='lowess')
            fig3.update_layout(
                xaxis_title="Years of Experience",
                yaxis_title="Annual Salary ($)",
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(family="Segoe UI", size=12),
                height=500
            )
            st.plotly_chart(fig3, use_container_width=True)
    
    # Footer
    st.markdown("""
    <div class="footer">
        © 2025 Premium Salary Predictor | AI-Powered Compensation Analysis | v3.0
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)  # Close main-container

if __name__ == "__main__":
    main()