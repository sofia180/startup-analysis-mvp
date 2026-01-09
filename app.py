import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------
# Page configuration
# --------------------
st.set_page_config(
    page_title="Startup Analysis MVP",
    layout="wide"
)

st.title("🚀 Startup Analysis MVP")
st.write(
    "This MVP demonstrates a basic analytical dashboard for evaluating startups "
    "based on funding, industry, and growth stage."
)

# --------------------
# Sample startup data
# --------------------
data = {
    "Startup": [
        "FinTechX",
        "HealthAI",
        "GreenEnergy",
        "EduTechPro",
        "CryptoPay"
    ],
    "Industry": [
        "FinTech",
        "HealthTech",
        "CleanTech",
        "EdTech",
        "Crypto"
    ],
    "Funding_USD_M": [
        12,
        8,
        15,
        5,
        20
    ],
    "Stage": [
        "Seed",
        "Series A",
        "Series B",
        "Seed",
        "Series C"
    ]
}

df = pd.DataFrame(data)

# --------------------
# Sidebar filters
# --------------------
st.sidebar.header("🔍 Filters")

industry_filter = st.sidebar.multiselect(
    "Select industry",
    options=df["Industry"].unique(),
    default=df["Industry"].unique()
)

filtered_df = df[df["Industry"].isin(industry_filter)]

# --------------------
# Data table
# --------------------
st.subheader("📊 Startup Dataset")
st.dataframe(filtered_df, use_container_width=True)

# --------------------
# Visualization
# --------------------
st.subheader("💰 Funding by Startup")

fig = px.bar(
    filtered_df,
    x="Startup",
    y="Funding_USD_M",
    color="Industry",
    title="Startup Funding (USD, Millions)"
)

st.plotly_chart(fig, use_container_width=True)

# --------------------
# Insights
# --------------------
st.subheader("📈 Key Insights")

st.write(
    f"""
    - Total startups analyzed: **{len(filtered_df)}**
    - Average funding: **{filtered_df['Funding_USD_M'].mean():.1f}M USD**
    - Highest funded startup: **{filtered_df.loc[filtered_df['Funding_USD_M'].idxmax(), 'Startup']}**
    """
)

st.markdown("---")
st.caption("MVP version · For educational and demonstration purposes")

