import pandas as pd
import numpy as np

from sklearn.preprocessing import FunctionTransformer, MinMaxScaler
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering#, KMedoids
# import hdbscan

import streamlit as st

class ClusteringPage:
    def __init__(self):
        self.data = None
        self.clustering_result = None

    def load_data(self, data):
        self.data = data

    def normalize_data(self, strategy):
        if strategy == "log":
            transformer = FunctionTransformer(np.log1p, validate=True)
            self.data = transformer.transform(self.data)
        elif strategy == "relative":
            self.data = self.data / self.data.sum(axis=0)
        elif strategy == "min-max":
            scaler = MinMaxScaler()
            self.data = scaler.fit_transform(self.data)

    def perform_clustering(self, algorithm):
        if algorithm == "k-means":
            clustering = KMeans()
        # elif algorithm == "k-medoids":
        #     clustering = KMedoids()
        elif algorithm == "dbscan":
            clustering = DBSCAN()
        elif algorithm == "hierarchical":
            clustering = AgglomerativeClustering()
        # elif algorithm == "hdbscan":
        #     clustering = hdbscan.HDBSCAN()
        self.clustering_result = clustering.fit_predict(self.data)

    def display_summary_statistics(self):
        st.write("Summary Statistics")
        st.dataframe(pd.DataFrame(self.clustering_result, columns=["Cluster"]).value_counts())

    def display_radar_chart(self):
        st.write("Radar Chart")
        # Add your own code to create the radar chart here

    def display_bar_graph(self):
        st.write("Bar Graph")
        # Add your own code to create the bar graph here

    def run(self):
        st.title("Clustering Page1")
        st.session_state["Clustering_status"] = True
        st.write(f"SESSION {st.session_state['Clustering_status']} in Clusering PAGE run")
        data = st.session_state.get("normalized_data")

        if data is None:
            st.warning("Please run the dataset page first to normalize the data.")
        else:
            self.load_data(data)
            algorithms = ["k-means", "k-medoids", "dbscan", "hierarchical", "hdbscan"]
            algorithm = st.radio("Clustering Algorithm", algorithms)
            self.perform_clustering(algorithm)
            self.display_summary_statistics()
            normalization_strategy = st.selectbox("Normalization Strategy", ["None", "Log", "Relative", "Min-Max"])
            if normalization_strategy != "None":
                self.normalize_data(normalization_strategy)
                self.display_radar_chart()
                self.display_bar_graph()
    
    def show(self):
        st.title("Clustering Page2")
        st.write(f"SESSION {st.session_state['Clustering_status']} in Clusering PAGE show")