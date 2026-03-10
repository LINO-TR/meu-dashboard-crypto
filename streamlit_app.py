import streamlit as st
import requests
from datetime import datetime

# Configuração de tela cheia para ver melhor no celular
st.set_page_config(page_title="Market Daily Dashboard", layout="wide")

st.title("📊 DASHBOARD DE ANÁLISE DIÁRIA")
st.caption(f"Foco: Macro, Baleias e Sentimento | {datetime.now().strftime('%d/%m/%Y %H:%M')}")

# --- 1. SENTIMENTO (FEAR & GREED) ---
st.header("1. Sentimento e Psicologia")
try:
    fng_url = "https://api.alternative.me/fng/"
    fng_data = requests.get(fng_url).json()['data'][0]
    val = int(fng_data['value'])
    status = fng_data['value_classification']
    
    col1, col2 = st.columns([1, 2])
    col1.metric("Fear & Greed Index", f"{val}/100", status)
    
    if val <= 25:
        col2.error("🎯 OPORTUNIDADE: Extremo Medo. Hora de procurar entradas.")
    elif val >= 75:
        col2.warning("📢 ALERTA: Extrema Ganância. Risco de correção iminente.")
    else:
        col2.info("⚖️ NEUTRO: Mercado aguardando definição.")
except:
    st.error("Erro ao carregar Fear & Greed")

st.divider()

# --- 2. MACRO E NOTÍCIAS (LINKS RÁPIDOS) ---
st.header("2. Macroeconomia e Notícias")
c1, c2 = st.columns(2)

with c1:
    st.subheader("🌐 Indicadores Chave")
    st.markdown("""
    - **[DXY (Dólar Mundial)](https://www.tradingview.com/symbols/DXY/)**: Se subir, BTC cai.
    - **[GOLD (Ouro)](https://www.tradingview.com/symbols/GOLD/)**: Busca por segurança.
    - **[US10Y (Juros EUA)](https://www.tradingview.com/symbols/TVC-US10Y/)**: Se subir, tira liquidez do BTC.
    """)

with c2:
    st.subheader("📅 Calendário Econômico")
    st.markdown("""
    - **[Investing.com (3 Estrelas)](https://br.investing.com/economic-calendar/)**
    - *O que buscar:* CPI (Inflação), FED (Juros), Payroll (Emprego).
    """)

st.divider()

# --- 3. BALEIAS E ON-CHAIN ---
st.header("3. Movimentação de Baleias")
b1, b2, b3 = st.columns(3)

with b1:
    st.markdown("### 🐳 Whale Alert")
    st.link_button("Ver Fluxo em Tempo Real", "https://whale-alert.io")
    st.caption("Carteira -> Exchange = Venda")

with b2:
    st.markdown("### 🕵️ Arkham Intel")
    st.link_button("Rastrear Grandes Fundos", "https://intel.arkm.com/explorer/entity/blackrock")
    st.caption("Veja BlackRock e MicroStrategy")

with b3:
    st.markdown("### 📉 CryptoQuant")
    st.link_button("Reservas das Corretoras", "https://cryptoquant.com/asset/btc/chart/exchange-flows")
    st.caption("Reservas caindo = Alta")

st.divider()

# --- 4. LIQUIDEZ E DERIVATIVOS ---
st.header("4. Liquidez (Onde o preço vai buscar)")
l1, l2 = st.columns(2)

with l1:
    st.subheader("🔥 Mapa de Liquidação")
    st.link_button("Abrir CoinGlass", "https://www.coinglass.com/pro/liquidation/Bitcoin")
    st.write("Procure as zonas de 'liquidez' (o preço caça os stops).")

with l2:
    st.subheader("⚡ Funding Rates")
    st.link_button("Ver Taxas de Financiamento", "https://www.coinglass.com/FundingRate")
    st.write("Taxas muito positivas = Mercado muito alavancado na compra.")

# --- ROTEIRO DE 5 MINUTOS (CHECKLIST) ---
st.sidebar.header("🚀 ROTEIRO DE 5 MINUTOS")
st.sidebar.checkbox("1. Sentimento (Fear & Greed)")
st.sidebar.checkbox("2. Macro (DXY e Juros)")
st.sidebar.checkbox("3. Notícias (Investing.com)")
st.sidebar.checkbox("4. Baleias (Whale Alert)")
st.sidebar.checkbox("5. Liquidez (CoinGlass)")

st.sidebar.success("Checklist concluído!")
