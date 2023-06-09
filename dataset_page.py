import pandas as pd
import numpy as np
# import os
# from pathlib import Path

from sklearn.preprocessing import FunctionTransformer, MinMaxScaler

import plotly.graph_objects as go
import streamlit as st

class DatasetPage:
    def __init__(self):
        # self.status = status
        # self.data = None
        self.normalized_data = None

    def load_data(self, file_path):
        st.session_state["df"] = pd.read_csv(file_path, sep=";")
    
    def normalize_data(self, strategy):
        if strategy == "log":
            transformer = FunctionTransformer(np.log1p, validate=True)
            self.normalized_data = transformer.transform(st.session_state["df"])
        elif strategy == "other":
            # Add your own normalization strategy here
            pass

    def display_summary_statistics(self):
        st.write("Summary Statistics")
        st.dataframe(st.session_state["df"].describe())

    def display_density_distribution_plot(self):
        st.write("Density Distribution Plot")
        fig = go.Figure()
        for column in st.session_state["df"].columns:
            fig.add_trace(go.Histogram(x=st.session_state["df"][column], name=column))
        st.plotly_chart(fig)
    
    # def __update_upload_file(self):


    def run(self):
        st.title("Dataset Page1")
        
        if "data" in st.session_state:
            st.file_uploader(f"Arquivo atual: {st.session_state.data.name}",
                                         type="csv",
                                         key="upload_file")
        else:
            st.file_uploader("Selecione o arquivo CSV", type="csv", key="upload_file")
        
        if st.session_state.upload_file is not None:
            st.session_state.data = st.session_state.upload_file

        if "data" in st.session_state:
            st.session_state.data.seek(0)# eliminar o buffer para nao quebrar o pd.read
            self.load_data(st.session_state.data)

            self.display_summary_statistics()
            strategy = st.selectbox("Normalization Strategy", ["None", "Log", "Other"])
            if strategy != "None":
                self.normalize_data(strategy)
                self.display_density_distribution_plot()