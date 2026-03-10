import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="Market Intelligence", layout="wide")

st.title("📊 Crypto & Macro Intelligence")
st.caption(f"Última atualização: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

def get_data():
    # Preço BTC e Variação
    cg_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_vol=true&include_24hr_change=true"
    data = requests.get(cg_url).json()['bitcoin']
    
    # Fear & Greed Index
    fng_url = "https://api.alternative.me/fng/"
    fng_data = requests.get(fng_url).json()['data'][0]
    
    return data, fng_data

try:
    btc, fng = get_data()

    # --- LINHA 1: Métricas Principais ---
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("BTC Preço", f"${btc['usd']:,.2f}", f"{btc['usd_24h_change']:.2f}%")
    
    with col2:
        st.metric("Sentimento do Mercado", f"{fng['value']}/100", fng['value_classification'])
        
    with col3:
        st.metric("Volume 24h", f"${btc['usd_24h_vol']/1e9:.2f}B")

    # --- LINHA 2: Análise e Insight ---
    st.divider()
    
    fng_val = int(fng['value'])
    if fng_val <= 25:
        st.error(f"🚨 **ANÁLISE:** MEDO EXTREMO. O varejo está em pânico. Históricamente, baleias utilizam essa liquidez para montar posições.")
    elif fng_val >= 75:
        st.warning(f"⚠️ **ANÁLISE:** GANÂNCIA EXTREMA. Risco de 'flush' (liquidação) para limpar os alavancados. Cautela em novas entradas.")
    else:
        st.info(f"⚖️ **ANÁLISE:** Mercado em equilíbrio. Monitorar rompimentos de suportes/resistências.")

    # --- LINHA 3: Gráfico de Sentimento (Gauge) ---
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = fng_val,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Índice de Medo e Ganância"},
        gauge = {
            'axis': {'range': [0, 100]},
            'bar': {'color': "black"},
            'steps': [
                {'range': [0, 25], 'color': "red"},
                {'range': [25, 50], 'color': "orange"},
                {'range': [50, 75], 'color': "yellow"},
                {'range': [75, 100], 'color': "green"}]
        }
    ))
    st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"Erro ao carregar dados: {e}")

st.sidebar.markdown("### 🔍 Fontes On-Chain")
st.sidebar.info("Dados via CoinGecko & Alternative.me")

