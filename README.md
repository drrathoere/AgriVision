# AgriVision: Plant Leaf Disease Classification Using Deep Learning

**Course:** CSE422 — Deep Learning  
**Academic session:** 2026–2027  
**University:** Lovely Professional University  
**Status:** Initial project scaffold — implementation in progress

## Overview
AgriVision is an academic project to classify plant leaf images into categories represented in a labelled dataset. It will use Python and TensorFlow/Keras to train a Convolutional Neural Network (CNN), evaluate predictions, and provide a simple interface for image upload and classification.

The project is intended for learning and demonstration. Predictions are not a substitute for professional agricultural advice.

## Objectives
- Prepare and inspect a labelled leaf-image dataset.
- Build a CNN image classifier using TensorFlow/Keras.
- Demonstrate convolution, activation, pooling, and dimensionality changes.
- Train using backpropagation and a gradient-based optimizer.
- Evaluate using accuracy, precision, recall, F1-score, and a confusion matrix.
- Optionally compare a custom CNN with transfer learning.
- Provide a Streamlit interface for inference after the model is trained.

## Dataset
A PlantVillage dataset variant or another appropriately licensed leaf-image dataset may be used. Confirm the selected dataset version, licence, labels, and class distribution before training.

Reference: https://github.com/spMohanty/PlantVillage-Dataset

## Initial structure
```text
AgriVision-CSE422/
├── README.md
├── requirements.txt
├── .gitignore
├── app.py
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── model.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
├── notebooks/
│   └── README.md
├── reports/
│   └── results.md
├── tests/
│   └── test_preprocessing.py
└── docs/
    └── index.html
```

## Setup
Use a Python version supported by the TensorFlow version you install.

```bash
python3 -m venv .venv
source .venv/bin/activate       # macOS/Linux
# .venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

## Planned workflow
1. Choose and document the dataset.
2. Create a reproducible train/validation/test split.
3. Implement preprocessing and the CNN model.
4. Train the model and save the best checkpoint locally.
5. Evaluate on the held-out test set and record actual metrics.
6. Run the Streamlit interface after a model checkpoint is available.

## Run the app
After implementing the model and training it:

```bash
streamlit run app.py
```

The initial `app.py` is a scaffold and will explain that a trained model is not yet available until training is implemented.

## Course-outcome alignment
- **CO1:** Supporting perceptron baseline experiment (planned).
- **CO2:** Track tensor shapes and dimensionality through network layers.
- **CO3:** Explain and apply backpropagation during training.
- **CO4:** Implement CNN components and examine feature maps.
- **CO5:** Use Python and TensorFlow/Keras for image classification.
- **CO6:** Optional separate RNN/LSTM/GRU experiment; not part of the initial CNN application.

## Evaluation
Record metrics only after running experiments. Do not report assumed accuracy. Planned metrics include accuracy, precision, recall, F1-score, confusion matrix, and training curves.

## Limitations
A model can only classify the categories represented in its training labels and may not generalize to different crops, conditions, or image backgrounds. Results depend on data quality, split strategy, and training settings.

## Academic information
- **Project:** AgriVision — Plant Leaf Disease Classification Using Deep Learning
- **Course:** CSE422 — Deep Learning
- **Student:** Navneet Nandan
- **Registration number:** To be added
- **Roll number:** To be added

## Status
This repository is an initial scaffold. Features, metrics, screenshots, and deployment status must be updated as they are implemented and tested.
