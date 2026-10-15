import streamlit as st

st.set_page_config(
    page_title="AgriVision | Plant Leaf Classification",
    page_icon="🌿",
    layout="wide",
)

st.title("🌿 AgriVision")
st.subheader("Plant Leaf Disease Classification Using Deep Learning")

st.info(
    "Initial project scaffold: the trained model and prediction pipeline have not "
    "been implemented yet. This interface is a starting point, not a working classifier."
)

st.markdown(
    """
    ### Project goals
    - Classify leaf images into dataset-defined categories.
    - Train and evaluate a CNN using TensorFlow/Keras.
    - Compare a custom CNN with transfer learning where feasible.
    - Explain model performance and limitations.

    ### Planned workflow
    1. Select and document a labelled dataset.
    2. Implement preprocessing and model training.
    3. Evaluate the trained model on held-out data.
    4. Add image upload and inference after a model checkpoint is available.
    """
)

st.caption("CSE422 — Deep Learning | Academic project under development")
