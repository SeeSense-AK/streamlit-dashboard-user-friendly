import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pydeck as pdk
from datetime import datetime, timedelta
import time
import json
import random
from typing import Dict, List, Tuple
import math

# Set page configuration
st.set_page_config(
    page_title="CycleSafe AI - Your Cycling Safety Navigator",
    page_icon="🚴‍♀️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for revolutionary UI
def load_revolutionary_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
        font-family: 'Inter', sans-serif;
    }
    
    .hero-section {
        background: rgba(255,255,255,0.95);
        border-radius: 20px;
        padding: 40px;
        margin: 20px 0;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
    }
    
    .ai-chat-container {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        border-radius: 15px;
        padding: 25px;
        margin: 20px 0;
        color: white;
        position: relative;
        overflow: hidden;
    }
    
    .ai-chat-container::before {
        content: '';
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1, #96ceb4);
        border-radius: 17px;
        z-index: -1;
        animation: gradient-shift 3s ease-in-out infinite;
    }
    
    @keyframes gradient-shift {
        0%, 100% { transform: rotate(0deg); }
        50% { transform: rotate(180deg); }
    }
    
    .story-card {
        background: rgba(255,255,255,0.9);
        border-radius: 15px;
        padding: 25px;
        margin: 15px 0;
        border-left: 5px solid #4facfe;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .story-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
    }
    
    .metric-hero {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        color: white;
        margin: 15px 0;
        position: relative;
        overflow: hidden;
    }
    
    .metric-hero::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: pulse 4s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 0.3; }
        50% { transform: scale(1.1); opacity: 0.1; }
    }
    
    .metric-value {
        font-size: 48px;
        font-weight: 700;
        margin-bottom: 10px;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    .metric-label {
        font-size: 16px;
        opacity: 0.9;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .insight-bubble {
        background: rgba(255,255,255,0.95);
        border-radius: 25px;
        padding: 20px;
        margin: 10px 0;
        border: 2px solid transparent;
        background-clip: padding-box;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        position: relative;
    }
    
    .insight-bubble::before {
        content: '';
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1);
        border-radius: 27px;
        z-index: -1;
        animation: rotate 3s linear infinite;
    }
    
    @keyframes rotate {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .progress-ring {
        transform: rotate(-90deg);
    }
    
    .progress-ring circle {
        stroke-dasharray: 251.2;
        stroke-dashoffset: 251.2;
        transition: stroke-dashoffset 2s ease-in-out;
    }
    
    .gamification-badge {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        border-radius: 50px;
        padding: 10px 20px;
        color: white;
        font-weight: 600;
        margin: 5px;
        display: inline-block;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .interactive-map-container {
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 15px 35px rgba(0,0,0,0.2);
        margin: 20px 0;
    }
    
    .ai-recommendation {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        padding: 20px;
        color: white;
        margin: 15px 0;
        position: relative;
    }
    
    .impact-simulator {
        background: rgba(255,255,255,0.95);
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
    }
    
    .scenario-button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border: none;
        border-radius: 10px;
        padding: 15px 25px;
        color: white;
        font-weight: 600;
        cursor: pointer;
        margin: 10px 5px;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .scenario-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    }
    
    .prediction-card {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        border-radius: 15px;
        padding: 25px;
        color: white;
        margin: 15px 0;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    
    .safety-score-container {
        position: relative;
        width: 200px;
        height: 200px;
        margin: 20px auto;
    }
    
    .floating-insight {
        position: fixed;
        top: 20px;
        right: 20px;
        background: rgba(255,255,255,0.95);
        border-radius: 15px;
        padding: 15px;
        max-width: 300px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        z-index: 1000;
        animation: float-in 0.5s ease-out;
    }
    
    @keyframes float-in {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    .stSelectbox > div > div {
        background: rgba(255,255,255,0.9);
        border-radius: 10px;
        border: 2px solid #4facfe;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border: none;
        border-radius: 10px;
        color: white;
        font-weight: 600;
        padding: 10px 20px;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    }
    
    .conversation-flow {
        background: rgba(255,255,255,0.9);
        border-radius: 20px;
        padding: 30px;
        margin: 20px 0;
        border: 1px solid rgba(255,255,255,0.3);
        backdrop-filter: blur(10px);
    }
    
    .typing-indicator {
        display: inline-block;
        animation: typing 1.5s infinite;
    }
    
    @keyframes typing {
        0%, 60%, 100% { opacity: 1; }
        30% { opacity: 0.5; }
    }
    </style>
    """, unsafe_allow_html=True)

# Simulated API calls and ML models
class CycleSafeAI:
    def __init__(self):
        self.conversations = []
        self.user_profile = {
            "role": "city_planner",
            "expertise": "beginner",
            "interests": ["safety", "infrastructure", "budget"]
        }
    
    def get_ai_insight(self, context: str) -> str:
        """Simulate Groq API call for AI insights"""
        insights = {
            "safety_score": [
                "Think of your city's cycling safety like a report card. You're currently at a B+ (8.4/10), which is good, but we can easily get you to an A!",
                "Your safety score of 8.4 means cyclists feel mostly safe, but there's room for improvement. Small changes can make a big difference.",
                "Imagine if every cyclist in your city felt as safe as walking in a park. We're 84% there - let's close that gap!"
            ],
            "hotspots": [
                "Picture this: You have 5 locations where cyclists hit the brakes hard - like speed bumps for bikes. These are your quick wins for safety improvements.",
                "Think of braking hotspots as 'ouch' moments for cyclists. The good news? Most can be fixed with simple visibility improvements.",
                "Your data shows cyclists are saying 'whoa!' at 250 locations. But here's the thing - 80% of incidents happen at just 20% of these spots."
            ],
            "predictions": [
                "Our AI crystal ball says: If you fix the top 3 problem areas, you'll prevent about 45 incidents next month. That's 45 people getting home safely!",
                "Based on patterns, next Tuesday around 5 PM will be your riskiest time. But we can change that with targeted improvements.",
                "The weather forecast shows rain on Thursday. Our model predicts 28% more incidents unless we act now."
            ]
        }
        return random.choice(insights.get(context, ["Great insight coming your way!"]))
    
    def generate_story(self, data_point: str) -> Dict:
        """Generate engaging stories from data"""
        stories = {
            "junction_safety": {
                "title": "The Story of Busy Corner",
                "narrative": "Meet Sarah, a daily commuter who cycles through Junction X every morning. Our data shows she and 247 other cyclists brake suddenly here each week. Why? The traffic light timing gives them just 8 seconds to cross safely. By adjusting it to 12 seconds, Sarah's commute becomes stress-free and 32% safer.",
                "impact": "247 cyclists affected daily",
                "solution": "Adjust signal timing",
                "cost": "$2,500",
                "benefit": "32% reduction in incidents"
            },
            "weather_impact": {
                "title": "The Rainy Day Challenge",
                "narrative": "When it rains, cyclists like Mike struggle with slippery surfaces on Oak Street. Our AI noticed that wet weather increases swerving by 40% here. Installing better drainage and non-slip surfaces would help Mike and 189 other regular cyclists stay upright and confident.",
                "impact": "189 cyclists affected in wet weather",
                "solution": "Improve drainage + non-slip surfaces",
                "cost": "$15,000",
                "benefit": "40% reduction in wet weather incidents"
            },
            "infrastructure_gap": {
                "title": "The Missing Link",
                "narrative": "Tom's safe bike lane suddenly ends at Pine Avenue, forcing him into traffic. This 200-meter gap causes 60% of cyclists to take risky maneuvers. Completing this missing link would create a continuous safe route for 500+ daily cyclists.",
                "impact": "500+ cyclists forced into traffic daily",
                "solution": "Complete protected bike lane",
                "cost": "$85,000",
                "benefit": "60% reduction in traffic conflicts"
            }
        }
        return stories.get(data_point, {})
    
    def predict_impact(self, intervention: str) -> Dict:
        """Simulate XGBoost predictions for impact assessment"""
        predictions = {
            "signal_timing": {
                "incident_reduction": 32,
                "cyclist_satisfaction": 85,
                "implementation_time": "2 weeks",
                "roi": "450%"
            },
            "protected_lanes": {
                "incident_reduction": 68,
                "cyclist_satisfaction": 92,
                "implementation_time": "3 months",
                "roi": "230%"
            },
            "surface_improvement": {
                "incident_reduction": 25,
                "cyclist_satisfaction": 78,
                "implementation_time": "1 month",
                "roi": "340%"
            }
        }
        return predictions.get(intervention, {})

# Initialize AI system
ai_system = CycleSafeAI()

# Load sample data with more realistic scenarios
@st.cache_data
def load_narrative_data():
    """Load data optimized for storytelling"""
    
    # Create realistic route data with personas
    route_stories = pd.DataFrame({
        'route_id': range(1, 1001),
        'route_name': [f"Route {i}" for i in range(1, 1001)],
        'primary_users': np.random.choice(['Commuters', 'Families', 'Fitness Enthusiasts', 'Students'], 1000),
        'safety_score': np.random.beta(3, 1, 1000) * 10,  # Skewed toward higher scores
        'daily_cyclists': np.random.poisson(50, 1000),
        'incident_rate': np.random.exponential(0.5, 1000),
        'infrastructure_quality': np.random.choice(['Excellent', 'Good', 'Fair', 'Poor'], 1000, p=[0.1, 0.3, 0.4, 0.2]),
        'weather_resilience': np.random.uniform(0.3, 1.0, 1000),
        'accessibility_score': np.random.uniform(0.2, 1.0, 1000),
        'community_priority': np.random.choice(['High', 'Medium', 'Low'], 1000, p=[0.2, 0.5, 0.3])
    })
    
    # Create hotspot data with contextual information
    hotspot_stories = pd.DataFrame({
        'location_id': range(1, 101),
        'location_name': [f"Location {i}" for i in range(1, 101)],
        'location_type': np.random.choice(['School Zone', 'Business District', 'Residential', 'Park Area', 'Transit Hub'], 100),
        'lat': np.random.uniform(51.5, 51.6, 100),
        'lon': np.random.uniform(-0.15, -0.05, 100),
        'risk_level': np.random.choice(['Critical', 'High', 'Medium', 'Low'], 100, p=[0.1, 0.2, 0.4, 0.3]),
        'affected_cyclists': np.random.poisson(30, 100),
        'incident_type': np.random.choice(['Sudden Braking', 'Swerving', 'Conflicts', 'Surface Issues'], 100),
        'time_of_day': np.random.choice(['Morning Rush', 'Midday', 'Evening Rush', 'Night'], 100),
        'fix_complexity': np.random.choice(['Quick Fix', 'Moderate', 'Complex'], 100, p=[0.4, 0.4, 0.2]),
        'estimated_cost': np.random.lognormal(8, 1, 100),  # Realistic cost distribution
        'community_impact': np.random.uniform(0.3, 1.0, 100)
    })
    
    return route_stories, hotspot_stories

# UI Components
def create_hero_section():
    """Create an engaging hero section"""
    st.markdown("""
    <div class="hero-section">
        <div style="text-align: center;">
            <h1 style="font-size: 3.5rem; margin-bottom: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">
                🚴‍♀️ CycleSafe AI Navigator
            </h1>
            <p style="font-size: 1.3rem; color: #666; max-width: 600px; margin: 0 auto;">
                Your intelligent companion for creating safer cycling environments. 
                We turn complex data into simple, actionable insights.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_ai_chat_interface():
    """Create an AI chat interface for natural interaction"""
    st.markdown("""
    <div class="ai-chat-container">
        <div style="display: flex; align-items: center; margin-bottom: 20px;">
            <div style="font-size: 2rem; margin-right: 15px;">🤖</div>
            <div>
                <h3 style="margin: 0;">Your AI Safety Assistant</h3>
                <p style="margin: 5px 0 0 0; opacity: 0.8;">Ask me anything about cycling safety in your city</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Chat interface
    user_question = st.text_input(
        "Ask your AI assistant:",
        placeholder="e.g., 'What's the biggest safety concern in my city?' or 'How can I improve cyclist safety with a $50k budget?'"
    )
    
    if user_question:
        with st.spinner("🤖 Thinking..."):
            time.sleep(1)  # Simulate processing
            
            # Generate contextual response
            if "budget" in user_question.lower():
                response = ai_system.get_ai_insight("budget_optimization")
            elif "safety" in user_question.lower():
                response = ai_system.get_ai_insight("safety_score")
            else:
                response = ai_system.get_ai_insight("general")
            
            st.success(f"🤖 AI Assistant: {response}")

def create_safety_score_wheel(score: float, target: float):
    """Create an animated safety score wheel"""
    fig = go.Figure()
    
    # Background circle
    fig.add_trace(go.Scatter(
        x=[0], y=[0],
        mode='markers',
        marker=dict(
            size=200,
            color='rgba(255,255,255,0.1)',
            line=dict(width=8, color='rgba(255,255,255,0.3)')
        ),
        showlegend=False
    ))
    
    # Score arc
    theta = np.linspace(0, 2*np.pi*score/10, 100)
    x = 0.8 * np.cos(theta)
    y = 0.8 * np.sin(theta)
    
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode='lines',
        line=dict(width=15, color='#4facfe'),
        showlegend=False
    ))
    
    # Center text
    fig.add_annotation(
        x=0, y=0,
        text=f"<b>{score:.1f}</b><br>Safety Score",
        showarrow=False,
        font=dict(size=24, color='white')
    )
    
    fig.update_layout(
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-1.2, 1.2]),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-1.2, 1.2]),
        height=200,
        margin=dict(l=0, r=0, t=0, b=0)
    )
    
    return fig

def create_story_card(story_data: Dict):
    """Create an engaging story card"""
    st.markdown(f"""
    <div class="story-card">
        <h3 style="color: #4facfe; margin-bottom: 15px;">📖 {story_data['title']}</h3>
        <p style="font-size: 16px; line-height: 1.6; margin-bottom: 20px;">
            {story_data['narrative']}
        </p>
        <div style="display: flex; justify-content: space-between; flex-wrap: wrap;">
            <div><strong>Impact:</strong> {story_data['impact']}</div>
            <div><strong>Solution:</strong> {story_data['solution']}</div>
            <div><strong>Cost:</strong> {story_data['cost']}</div>
            <div><strong>Benefit:</strong> {story_data['benefit']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_impact_simulator():
    """Create an interactive impact simulator"""
    st.markdown("""
    <div class="impact-simulator">
        <h3 style="text-align: center; margin-bottom: 30px;">🎯 Impact Simulator</h3>
        <p style="text-align: center; margin-bottom: 30px;">
            See the real-world impact of your safety investments
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <button class="scenario-button" onclick="simulate('signals')">
            🚦 Better Traffic Signals
        </button>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <button class="scenario-button" onclick="simulate('lanes')">
            🛣️ Protected Bike Lanes
        </button>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <button class="scenario-button" onclick="simulate('surface')">
            🔧 Surface Improvements
        </button>
        """, unsafe_allow_html=True)
    
    # Simulation results
    intervention = st.selectbox(
        "Select an intervention to simulate:",
        ["Traffic Signal Optimization", "Protected Bike Lanes", "Surface Improvements"],
        index=0
    )
    
    if intervention == "Traffic Signal Optimization":
        results = ai_system.predict_impact("signal_timing")
        st.markdown(f"""
        <div class="prediction-card">
            <h4>Predicted Impact: Traffic Signal Optimization</h4>
            <div style="display: flex; justify-content: space-around; margin-top: 20px;">
                <div>
                    <div style="font-size: 2rem; font-weight: bold;">{results['incident_reduction']}%</div>
                    <div>Incident Reduction</div>
                </div>
                <div>
                    <div style="font-size: 2rem; font-weight: bold;">{results['cyclist_satisfaction']}%</div>
                    <div>Cyclist Satisfaction</div>
                </div>
                <div>
                    <div style="font-size: 2rem; font-weight: bold;">{results['roi']}</div>
                    <div>Return on Investment</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def create_gamified_dashboard():
    """Create gamified elements for engagement"""
    st.markdown("""
    <div style="text-align: center; margin: 30px 0;">
        <h3>🏆 Your Safety Achievement Level</h3>
        <div style="margin: 20px 0;">
            <span class="gamification-badge">🥉 Bronze Safety Champion</span>
            <span class="gamification-badge">🎯 Problem Solver</span>
            <span class="gamification-badge">📈 Data Explorer</span>
        </div>
        <p style="color: #666;">
            Complete 2 more safety improvements to unlock <strong>Silver Safety Champion</strong> badge!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Progress bar
    progress = 0.7
    st.progress(progress, text="Progress to next level: 70%")

def create_priority_matrix():
    """Create a simple priority matrix for decision making"""
    st.markdown("""
    <div class="conversation-flow">
        <h3>🎯 Your Top 3 Quick Wins</h3>
        <p>Based on your data, here are the most impactful changes you can make:</p>
    </div>
    """, unsafe_allow_html=True)
    
    priorities = [
        {
            "rank": 1,
            "action": "Adjust traffic signal timing at Main & Oak",
            "effort": "Low",
            "impact": "High",
            "timeline": "2 weeks",
            "cost": "$2,500"
        },
        {
            "rank": 2,
            "action": "Install 'Cyclists Present' warning signs",
            "effort": "Low",
            "impact": "Medium",
            "timeline": "1 week",
            "cost": "$800"
        },
        {
            "rank": 3,
            "action": "Repair surface on Pine Street bike lane",
            "effort": "Medium",
            "impact": "Medium",
            "timeline": "3 weeks",
            "cost": "$12,000"
        }
    ]
    
    for priority in priorities:
        st.markdown(f"""
        <div class="insight-bubble">
            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                <div style="background: #4facfe; color: white; border-radius: 50%; width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; margin-right: 15px; font-weight: bold;">
                    {priority['rank']}
                </div>
                <h4 style="margin: 0; color: #333;">{priority['action']}</h4>
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 14px; color: #666;">
                <span>⚡ Effort: {priority['effort']}</span>
                <span>📈 Impact: {priority['impact']}</span>
                <span>⏱️ Timeline: {priority['timeline']}</span>
                <span>💰 Cost: {priority['cost']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

def create_before_after_visualization():
    """Create before/after visualization"""
    st.markdown("""
    <div class="conversation-flow">
        <h3>🔄 Before & After: See the Difference</h3>
        <p>Here's what your city looks like today vs. after implementing our recommendations:</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 20px; background: #ffe6e6; border-radius: 15px; margin: 10px 0;">
            <h4 style="color: #d9534f;">😰 Current State</h4>
            <div style="font-size: 2rem; margin: 10px 0;">8.4/10</div>
            <p>Safety Score</p>
            <div style="font-size: 1.5rem; margin: 10px 0;">47</div>
            <p>Monthly Incidents</p>
            <div style="font-size: 1.5rem; margin: 10px 0;">73%</div>
            <p>Cyclist Confidence</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 20px; background: #e6ffe6; border-radius: 15px; margin: 10px 0;">
            <h4 style="color: #5cb85c;">😊 After Improvements</h4>
            <div style="font-size: 2rem; margin: 10px 0;">9.2/10</div>
            <p>Safety Score</p>
            <div style="font-size: 1.5rem; margin: 10px 0;">28</div>
            <p>Monthly Incidents</p>
            <div style="font-size: 1.5rem; margin: 10px 0;">91%</div>
            <p>Cyclist Confidence</p>
        </div>
        """, unsafe_allow_html=True)

def create_conversational_insights():
    """Create conversational insights that feel like talking to a friend"""
    st.markdown("""
    <div class="ai-chat-container">
        <div style="display: flex; align-items: center; margin-bottom: 15px;">
            <span style="font-size: 1.5rem; margin-right: 10px;">💡</span>
            <h4 style="margin: 0;">What Your Data is Really Saying</h4>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    insights = [
        {
            "emoji": "🚦",
            "title": "Traffic Signals Need Love",
            "message": "Your cyclists are hitting the brakes at 5 intersections way more than they should. It's like having stop signs where there should be yield signs. A simple timing adjustment could make everyone's day better!",
            "action": "Quick 2-week fix for $2,500"
        },
        {
            "emoji": "🌧️",
            "title": "Rainy Day Blues",
            "message": "When it rains, your cyclists become wobbly - swerving increases by 40% on Oak Street. Think of it like ice skating in sneakers. Better drainage could change everything.",
            "action": "Weather-proof your routes for $15K"
        },
        {
            "emoji": "👥",
            "title": "Your Cyclist Community",
            "message": "You have 3 main groups: Morning Commuters (speed demons), Family Riders (safety first), and Fitness Enthusiasts (weekend warriors). Each group needs different things to feel safe.",
            "action": "Tailored safety for each group"
        }
    ]
    
    for insight in insights:
        st.markdown(f"""
        <div class="story-card">
            <div style="display: flex; align-items: center; margin-bottom: 15px;">
                <span style="font-size: 2rem; margin-right: 15px;">{insight['emoji']}</span>
                <h4 style="margin: 0; color: #4facfe;">{insight['title']}</h4>
            </div>
            <p style="font-size: 16px; line-height: 1.6; margin-bottom: 15px;">
                {insight['message']}
            </p>
            <div style="background: #f8f9fa; padding: 10px; border-radius: 8px; border-left: 4px solid #4facfe;">
                <strong>💪 Action:</strong> {insight['action']}
            </div>
        </div>
        """, unsafe_allow_html=True)

def create_smart_recommendations():
    """Create AI-powered smart recommendations"""
    st.markdown("""
    <div class="ai-recommendation">
        <h3 style="margin-bottom: 20px;">🎯 Your Personalized Action Plan</h3>
        <p style="margin-bottom: 20px; opacity: 0.9;">
            Based on your role as a city planner and your $50K budget, here's what our AI recommends:
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    recommendations = [
        {
            "priority": "🔥 URGENT",
            "action": "Fix the 'Death Junction' at Main & Oak",
            "reason": "247 cyclists brake hard here daily - it's your #1 safety concern",
            "cost": "$2,500",
            "timeframe": "2 weeks",
            "impact": "Prevents ~15 incidents/month"
        },
        {
            "priority": "💪 HIGH IMPACT",
            "action": "Complete the missing bike lane link on Pine St",
            "reason": "500+ cyclists forced into traffic daily at this gap",
            "cost": "$35,000",
            "timeframe": "6 weeks",
            "impact": "Protects 500+ daily cyclists"
        },
        {
            "priority": "🌟 QUICK WIN",
            "action": "Install smart warning signs at 8 locations",
            "reason": "Low cost, high visibility safety improvement",
            "cost": "$8,000",
            "timeframe": "1 week",
            "impact": "Increases driver awareness 3x"
        }
    ]
    
    for i, rec in enumerate(recommendations, 1):
        st.markdown(f"""
        <div class="insight-bubble">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                <h4 style="margin: 0; color: #333;">#{i} {rec['action']}</h4>
                <span style="background: #4facfe; color: white; padding: 5px 10px; border-radius: 15px; font-size: 12px; font-weight: bold;">
                    {rec['priority']}
                </span>
            </div>
            <p style="margin-bottom: 15px; color: #666; font-style: italic;">
                "{rec['reason']}"
            </p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(120px, 1fr)); gap: 10px; font-size: 14px;">
                <div><strong>💰 Cost:</strong> {rec['cost']}</div>
                <div><strong>⏱️ Time:</strong> {rec['timeframe']}</div>
                <div><strong>📈 Impact:</strong> {rec['impact']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Budget tracker
    total_cost = 2500 + 35000 + 8000
    remaining_budget = 50000 - total_cost
    
    st.markdown(f"""
    <div style="background: #e8f5e8; padding: 20px; border-radius: 15px; margin: 20px 0; text-align: center;">
        <h4 style="color: #2d5a2d; margin-bottom: 15px;">💰 Budget Tracker</h4>
        <div style="display: flex; justify-content: space-around;">
            <div>
                <div style="font-size: 1.5rem; font-weight: bold; color: #2d5a2d;">${total_cost:,}</div>
                <div style="color: #666;">Recommended Spend</div>
            </div>
            <div>
                <div style="font-size: 1.5rem; font-weight: bold; color: #2d5a2d;">${remaining_budget:,}</div>
                <div style="color: #666;">Remaining Budget</div>
            </div>
            <div>
                <div style="font-size: 1.5rem; font-weight: bold; color: #2d5a2d;">91%</div>
                <div style="color: #666;">Budget Efficiency</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_interactive_map_with_stories():
    """Create an interactive map that tells stories"""
    st.markdown("""
    <div class="interactive-map-container">
        <h3 style="text-align: center; padding: 20px; margin: 0; background: rgba(79, 172, 254, 0.1);">
            🗺️ Your City's Safety Story Map
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Create sample map data with stories
    map_data = pd.DataFrame({
        'lat': [51.5074, 51.5155, 51.5033, 51.5200, 51.5085],
        'lon': [-0.1278, -0.1123, -0.1195, -0.1050, -0.1400],
        'name': ['Death Junction', 'School Zone Chaos', 'Pothole Paradise', 'Rush Hour Nightmare', 'Weather Trap'],
        'story': [
            'Sarah hits the brakes here every morning - 247 cyclists do the same',
            'Parents avoid this route with kids - visibility issues at drop-off time',
            'Mike\'s bike tire got damaged here last week - rough surface conditions',
            'Evening commuters bottleneck here - needs better traffic flow',
            'Emma slips here when it rains - drainage problems'
        ],
        'severity': [9, 7, 6, 8, 7],
        'affected_daily': [247, 156, 89, 312, 134],
        'fix_cost': [2500, 15000, 12000, 45000, 18000]
    })
    
    # Create the map
    fig = px.scatter_mapbox(
        map_data,
        lat="lat",
        lon="lon",
        size="affected_daily",
        color="severity",
        hover_name="name",
        hover_data={
            "story": True,
            "affected_daily": True,
            "fix_cost": True,
            "lat": False,
            "lon": False
        },
        color_continuous_scale="Reds",
        size_max=25,
        zoom=12,
        mapbox_style="carto-positron",
        title="Click on any hotspot to hear its story"
    )
    
    fig.update_layout(
        height=500,
        margin=dict(l=0, r=0, t=30, b=0)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Story selector
    selected_location = st.selectbox(
        "🎭 Choose a location to hear its story:",
        options=map_data['name'].tolist(),
        index=0
    )
    
    if selected_location:
        location_data = map_data[map_data['name'] == selected_location].iloc[0]
        
        st.markdown(f"""
        <div class="story-card">
            <h4 style="color: #4facfe; margin-bottom: 15px;">📍 {location_data['name']}</h4>
            <p style="font-size: 16px; line-height: 1.6; margin-bottom: 20px;">
                {location_data['story']}
            </p>
            <div style="display: flex; justify-content: space-between; flex-wrap: wrap; background: #f8f9fa; padding: 15px; border-radius: 8px;">
                <div><strong>Daily Impact:</strong> {location_data['affected_daily']} cyclists</div>
                <div><strong>Severity:</strong> {location_data['severity']}/10</div>
                <div><strong>Fix Cost:</strong> ${location_data['fix_cost']:,}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

def create_progress_tracking():
    """Create progress tracking with celebration"""
    st.markdown("""
    <div class="conversation-flow">
        <h3>📊 Your Safety Journey Progress</h3>
        <p>Track your improvements and celebrate every win!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Create progress metrics
    progress_data = {
        "Overall Safety Score": {"current": 8.4, "target": 9.5, "unit": "/10"},
        "Monthly Incidents": {"current": 47, "target": 25, "unit": "", "reverse": True},
        "Cyclist Confidence": {"current": 73, "target": 90, "unit": "%"},
        "Infrastructure Quality": {"current": 6.8, "target": 8.5, "unit": "/10"}
    }
    
    cols = st.columns(2)
    
    for i, (metric, data) in enumerate(progress_data.items()):
        with cols[i % 2]:
            if data.get("reverse"):
                progress = max(0, (data["current"] - data["target"]) / data["current"])
                progress_pct = (1 - progress) * 100
            else:
                progress = min(1, data["current"] / data["target"])
                progress_pct = progress * 100
            
            st.markdown(f"""
            <div style="background: white; padding: 20px; border-radius: 15px; margin: 10px 0; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                <h4 style="margin-bottom: 15px; color: #333;">{metric}</h4>
                <div style="display: flex; justify-content: space-between; margin-bottom: 10px;">
                    <span style="font-size: 1.5rem; font-weight: bold; color: #4facfe;">
                        {data['current']}{data['unit']}
                    </span>
                    <span style="color: #666;">
                        Target: {data['target']}{data['unit']}
                    </span>
                </div>
                <div style="background: #e9ecef; height: 10px; border-radius: 5px; overflow: hidden;">
                    <div style="background: linear-gradient(90deg, #4facfe, #00f2fe); height: 100%; width: {progress_pct}%; transition: width 1s ease;"></div>
                </div>
                <div style="text-align: center; margin-top: 10px; font-size: 14px; color: #666;">
                    {progress_pct:.0f}% to target
                </div>
            </div>
            """, unsafe_allow_html=True)

def create_celebration_moments():
    """Create celebration moments for achievements"""
    achievements = [
        "🎉 Reduced incidents by 15% this month!",
        "🌟 Completed 3 safety improvements ahead of schedule!",
        "🏆 Achieved highest cyclist satisfaction rating in 2 years!",
        "💪 Prevented an estimated 23 incidents with recent changes!"
    ]
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #ffeaa7, #fab1a0); padding: 25px; border-radius: 20px; margin: 20px 0; text-align: center;">
        <h3 style="margin-bottom: 20px; color: #2d3436;">🎊 Recent Achievements</h3>
    """, unsafe_allow_html=True)
    
    for achievement in achievements:
        st.markdown(f"""
        <div style="background: rgba(255,255,255,0.8); padding: 10px; margin: 8px 0; border-radius: 10px;">
            {achievement}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

def main():
    # Load CSS
    load_revolutionary_css()
    
    # Load data
    route_data, hotspot_data = load_narrative_data()
    
    # Create hero section
    create_hero_section()
    
    # AI Chat Interface
    st.markdown("## 🤖 Start with a Question")
    create_ai_chat_interface()
    
    # Main dashboard tabs with user-friendly names
    tabs = st.tabs([
        "🏠 My City Dashboard", 
        "📖 Safety Stories", 
        "🎯 Action Plan",
        "📊 Progress Tracker",
        "🎮 What-If Simulator"
    ])
    
    # Tab 1: My City Dashboard
    with tabs[0]:
        st.markdown("## 🏙️ Your City at a Glance")
        
        # Key metrics in an engaging way
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="metric-hero">
                <div class="metric-value">8.4</div>
                <div class="metric-label">Safety Score</div>
                <div style="font-size: 14px; margin-top: 10px; opacity: 0.8;">
                    📈 +0.6 this month
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="metric-hero">
                <div class="metric-value">2,847</div>
                <div class="metric-label">Daily Cyclists</div>
                <div style="font-size: 14px; margin-top: 10px; opacity: 0.8;">
                    🚴 +12% vs last year
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="metric-hero">
                <div class="metric-value">5</div>
                <div class="metric-label">Priority Areas</div>
                <div style="font-size: 14px; margin-top: 10px; opacity: 0.8;">
                    🎯 Quick wins available
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Conversational insights
        create_conversational_insights()
        
        # Interactive map with stories
        create_interactive_map_with_stories()
        
        # Gamification elements
        create_gamified_dashboard()
    
    # Tab 2: Safety Stories
    with tabs[1]:
        st.markdown("## 📚 Your City's Safety Stories")
        st.markdown("Every data point represents real people. Here are their stories:")
        
        # Story selection
        story_type = st.selectbox(
            "Choose a story to explore:",
            ["The Junction Problem", "Rainy Day Challenges", "The Missing Link"],
            index=0
        )
        
        if story_type == "The Junction Problem":
            story_data = ai_system.generate_story("junction_safety")
        elif story_type == "Rainy Day Challenges":
            story_data = ai_system.generate_story("weather_impact")
        else:
            story_data = ai_system.generate_story("infrastructure_gap")
        
        if story_data:
            create_story_card(story_data)
        
        # Before and after visualization
        create_before_after_visualization()
        
        # User personas and their journeys
        st.markdown("### 👥 Meet Your Cyclists")
        
        personas = [
            {
                "name": "Sarah the Commuter",
                "emoji": "👩‍💼",
                "description": "Cycles 8km daily to work, values speed and predictability",
                "main_concern": "Traffic signal timing and junction safety",
                "current_satisfaction": "7/10"
            },
            {
                "name": "Mike the Family Man",
                "emoji": "👨‍👩‍👧‍👦",
                "description": "Weekend rides with kids, prioritizes safety above all",
                "main_concern": "Protected lanes and surface quality",
                "current_satisfaction": "6/10"
            },
            {
                "name": "Emma the Fitness Enthusiast",
                "emoji": "🏃‍♀️",
                "description": "Long recreational rides, loves exploring new routes",
                "main_concern": "Route connectivity and weather resilience",
                "current_satisfaction": "8/10"
            }
        ]
        
        for persona in personas:
            st.markdown(f"""
            <div class="story-card">
                <div style="display: flex; align-items: center; margin-bottom: 15px;">
                    <span style="font-size: 3rem; margin-right: 20px;">{persona['emoji']}</span>
                    <div>
                        <h4 style="margin: 0; color: #4facfe;">{persona['name']}</h4>
                        <p style="margin: 5px 0; color: #666;">{persona['description']}</p>
                    </div>
                </div>
                <div style="background: #f8f9fa; padding: 15px; border-radius: 8px;">
                    <p><strong>Main Concern:</strong> {persona['main_concern']}</p>
                    <p><strong>Current Satisfaction:</strong> {persona['current_satisfaction']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Tab 3: Action Plan
    with tabs[2]:
        st.markdown("## 🎯 Your Personalized Action Plan")
        
        # Smart recommendations
        create_smart_recommendations()
        
        # Priority matrix
        create_priority_matrix()
        
        # Implementation timeline
        st.markdown("### 📅 Implementation Timeline")
        
        timeline_data = [
            {"week": "Week 1", "action": "Install warning signs", "status": "ready"},
            {"week": "Week 2-3", "action": "Adjust traffic signals", "status": "ready"},
            {"week": "Week 4-7", "action": "Repair surface issues", "status": "planning"},
            {"week": "Week 8-14", "action": "Complete bike lane gap", "status": "planning"},
        ]
        
        for item in timeline_data:
            status_color = "#28a745" if item["status"] == "ready" else "#ffc107"
            status_text = "✅ Ready to Start" if item["status"] == "ready" else "📋 In Planning"
            
            st.markdown(f"""
            <div style="display: flex; align-items: center; padding: 15px; background: white; border-radius: 10px; margin: 10px 0; border-left: 4px solid {status_color};">
                <div style="font-weight: bold; color: #333; min-width: 100px;">{item['week']}</div>
                <div style="flex: 1; margin: 0 20px;">{item['action']}</div>
                <div style="color: {status_color}; font-weight: 500;">{status_text}</div>
            </div>
            """, unsafe_allow_html=True)
    
    # Tab 4: Progress Tracker
    with tabs[3]:
        st.markdown("## 📈 Track Your Success")
        
        # Progress tracking
        create_progress_tracking()
        
        # Celebration moments
        create_celebration_moments()
        
        # Trend analysis in simple terms
        st.markdown("### 📊 Your Safety Trends")
        
        # Create simple trend chart
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        incidents = [65, 58, 52, 48, 45, 47]
        satisfaction = [68, 71, 74, 76, 78, 73]
        
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        
        fig.add_trace(
            go.Scatter(x=months, y=incidents, name="Monthly Incidents", 
                      line=dict(color='#e74c3c', width=3), mode='lines+markers'),
            secondary_y=False,
        )
        
        fig.add_trace(
            go.Scatter(x=months, y=satisfaction, name="Cyclist Satisfaction", 
                      line=dict(color='#2ecc71', width=3), mode='lines+markers'),
            secondary_y=True,
        )
        
        fig.update_xaxes(title_text="Month")
        fig.update_yaxes(title_text="Number of Incidents", secondary_y=False)
        fig.update_yaxes(title_text="Satisfaction (%)", secondary_y=True)
        
        fig.update_layout(
            title="Your City's Safety Journey",
            height=400,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.info("📈 **What this means:** You're on the right track! Incidents are decreasing, but May's dip in satisfaction suggests we need to focus on cyclist experience, not just numbers.")
    
    # Tab 5: What-If Simulator
    with tabs[4]:
        st.markdown("## 🎮 What-If Simulator")
        st.markdown("Play with different scenarios to see their impact before you invest!")
        
        # Impact simulator
        create_impact_simulator()
        
        # Interactive scenario builder
        st.markdown("### 🔧 Build Your Own Scenario")
        
        col1, col2 = st.columns(2)
        
        with col1:
            budget = st.slider("Available Budget ($)", 10000, 200000, 50000, 5000)
            timeframe = st.selectbox("Implementation Timeframe", ["1 month", "3 months", "6 months", "1 year"])
            priority = st.selectbox("Main Priority", ["Reduce incidents", "Improve satisfaction", "Increase ridership"])
        
        with col2:
            st.markdown("### 🎯 Scenario Results")
            
            # Calculate scenario results based on inputs
            if budget >= 45000:
                impact_level = "High"
                incident_reduction = 45
                satisfaction_boost = 18
            elif budget >= 25000:
                impact_level = "Medium"
                incident_reduction = 28
                satisfaction_boost = 12
            else:
                impact_level = "Low"
                incident_reduction = 15
                satisfaction_boost = 8
            
            st.markdown(f"""
            <div class="prediction-card">
                <h4>Predicted Impact: {impact_level}</h4>
                <div style="margin-top: 20px;">
                    <div style="font-size: 1.5rem; font-weight: bold; margin-bottom: 10px;">
                        -{incident_reduction}% incidents
                    </div>
                    <div style="font-size: 1.5rem; font-weight: bold; margin-bottom: 10px;">
                        +{satisfaction_boost}% satisfaction
                    </div>
                    <div style="font-size: 1.5rem; font-weight: bold;">
                        ROI: {random.randint(200, 400)}%
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Scenario comparison
        st.markdown("### ⚖️ Compare Scenarios")
        
        scenarios = pd.DataFrame({
            'Scenario': ['Quick Fixes Only', 'Balanced Approach', 'Major Infrastructure'],
            'Cost': ['$15K', '$50K', '$150K'],
            'Incident Reduction': ['15%', '32%', '68%'],
            'Timeline': ['1 month', '3 months', '12 months'],
            'Difficulty': ['Easy', 'Medium', 'Complex']
        })
        
        st.dataframe(scenarios, use_container_width=True)
        
        # Final AI recommendation
        st.markdown("""
        <div class="ai-recommendation">
            <h4>🤖 AI Recommendation for Your Scenario</h4>
            <p>
                Based on your budget of ${:,} and focus on {}, I recommend the <strong>Balanced Approach</strong>. 
                You'll see meaningful results within 3 months while staying within budget. 
                This gives you the best bang for your buck and sets you up for bigger wins later!
            </p>
        </div>
        """.format(budget, priority.lower()), unsafe_allow_html=True)
    
    # Footer with support
    st.markdown("""
    <div style="text-align: center; margin-top: 50px; padding: 30px; background: rgba(255,255,255,0.9); border-radius: 20px;">
        <h4 style="color: #4facfe; margin-bottom: 15px;">Need Help? We're Here for You! 🤝</h4>
        <p style="color: #666; margin-bottom: 20px;">
            Our AI assistant is available 24/7, and our expert team is just a click away.
        </p>
        <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
            <button style="background: #4facfe; color: white; border: none; padding: 10px 20px; border-radius: 25px; cursor: pointer;">
                💬 Chat with AI
            </button>
            <button style="background: #2ecc71; color: white; border: none; padding: 10px 20px; border-radius: 25px; cursor: pointer;">
                📞 Schedule Expert Call
            </button>
            <button style="background: #e74c3c; color: white; border: none; padding: 10px 20px; border-radius: 25px; cursor: pointer;">
                📚 Access Help Center
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
