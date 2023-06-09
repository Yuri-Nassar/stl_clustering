import streamlit as st

from dataset_page import DatasetPage
from clustering_page import ClusteringPage

class App:
    def __init__(self):
        self.pages = {
            "Dataset": DatasetPage,
            "Clustering": ClusteringPage
        }

    def run(self):
        st.sidebar.title("Navigation")
        st.write(f"session_state: {st.session_state}")
        page = st.sidebar.radio("Go to", list(self.pages.keys()))
        # self.pages[page]()#.run()

        
        with st.spinner(f"Loading {page}..."):
            self.pages[page]().run()
            # if st.session_state.get(page+"_status"):
            #     st.write(f"SESSION {self.st_obj.status[page+'_status']} in APP_PAGE")
            #     self.pages[page](self.st_obj.status[page+'_status']).show()
            # else:
            #     st.write(f"SESSION {self.st_obj.status[page+'_status']} in APP_PAGE")
            #     self.pages[page](self.st_obj.status[page+'_status']).run()