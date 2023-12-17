import streamlit as st
import pandas as pd
import datetime
import os
filePath = "./data/masterdf.parquet"
st.set_page_config(layout="wide")
goals_data = pd.read_parquet(filePath)
preds = pd.DataFrame({
    "LM" : ["Bruno Fernandes", "V. van Dijk", "Rúben Dias", "Rodri"], 
    "SS" : ["Bruno Fernandes", "V. van Dijk", "T. Alexander-Arnold", "S. March"], 
    "DH" : ["D. Szoboszlai", "A. Lallana", "Casemiro", "Y. Tielemans"],
    "JM" : ["A. Mac Allister", "V. van Dijk", "T. Alexander-Arnold", "C. Jones"],
    "SM" : ["A. Mac Allister", "Joelinton", "M. Jensen", "T. Alexander-Arnold"]
    })

# for player in preds.columns:
#     print(goals_data[goals_data["player.name"].isin(preds[player])][["player.name", "goals.total"]])

SM, SS, DH, LM, JM = st.columns(5)

with SM:
    player = "SM"   
    df = goals_data[(goals_data["player.name"].isin(preds[player]))&(goals_data["league.id"]==39)][["player.name", "goals.total"]]    
    df.columns = ["Player", "Goals"]
    st.header(player)
    st.header(df["Goals"].sum().astype(int))
    st.dataframe(df.sort_values("Goals", ascending = False), hide_index = True)

with SS:
    player = "SS"   
    df = goals_data[(goals_data["player.name"].isin(preds[player]))&(goals_data["league.id"]==39)][["player.name", "goals.total"]]    
    df.columns = ["Player", "Goals"]
    st.header(player)
    st.header(df["Goals"].sum().astype(int))
    st.dataframe(df.sort_values("Goals", ascending = False), hide_index = True)

with DH:
    player = "DH"   
    df = goals_data[(goals_data["player.name"].isin(preds[player]))&(goals_data["league.id"]==39)][["player.name", "goals.total"]]    
    df.columns = ["Player", "Goals"]
    st.header(player)
    st.header(df["Goals"].sum().astype(int))
    st.dataframe(df.sort_values("Goals", ascending = False), hide_index = True)

with LM:
    player = "LM"   
    df = goals_data[(goals_data["player.name"].isin(preds[player]))&(goals_data["league.id"]==39)][["player.name", "goals.total"]]    
    df.columns = ["Player", "Goals"]
    st.header(player)
    st.header(df["Goals"].sum().astype(int))
    st.dataframe(df.sort_values("Goals", ascending = False), hide_index = True)
     
with JM:
    player = "JM"   
    df = goals_data[(goals_data["player.name"].isin(preds[player]))&(goals_data["league.id"]==39)][["player.name", "goals.total"]]    
    df.columns = ["Player", "Goals"]
    st.header(player)
    st.header(df["Goals"].sum().astype(int))
    st.dataframe(df.sort_values("Goals", ascending = False), hide_index = True)

st.text(f"Last refresh: {datetime.datetime.fromtimestamp(os.path.getmtime(filePath))}")