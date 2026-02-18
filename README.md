# Second Kaggle Submission - MNIST Digit Classification

## Project Overview
This project implements machine learning models for handwritten digit classification using the MNIST dataset. The pipeline includes exploratory data analysis, feature engineering, and model training with multiple algorithms.

## Project Structure
```
├── data/                       # Dataset files
│   ├── train.csv              # Training data
│   ├── test.csv               # Test data
│   ├── train_processed.csv    # Normalized training data
│   ├── test_processed.csv     # Normalized test data
│   └── sample_submission.csv  # Submission template
├── notebooks/                  # Jupyter notebooks
│   ├── 01_eda.ipynb           # Exploratory Data Analysis
│   ├── 02_feature_engineering.ipynb  # Data preprocessing
│   └── 03_modelling.ipynb     # Model training and evaluation
├── src/                        # Source code
│   └── preprocessor.py        # Data normalization utilities
├── README.md                   # Project documentation
└── RESULTS.md                  # Model performance results
```

## Models Implemented

### 1. Random Forest Classifier
- **Cross-validation scores**: [0.959, 0.965, 0.961, 0.960, 0.964]
- **Mean Accuracy**: 96.17%
- **Standard Deviation**: 0.0021

### 2. Logistic Regression
- **Solver**: SAGA (multinomial classification)
- **Cross-validation scores**: [0.919, 0.920, 0.909, 0.913, 0.916]
- **Mean Accuracy**: 91.54%
- **Standard Deviation**: 0.0039

### 3. Neural Network (PyTorch)
- Architecture: Fully connected layers (784 → 12 → 10)
- Activation: ReLU
- Dropout: 0.2
- Optimizer: Adam (lr=0.01)

## Data Preprocessing
- **Normalization**: Pixel values scaled from [0, 255] to [0, 1]
- **Train-Test Split**: 80-20 split with stratification
- **Image Size**: 28x28 pixels (784 features)

## Installation & Usage
```bash
# Install required packages
pip install pandas numpy scikit-learn torch matplotlib seaborn
```

## Author
Ian Muchesia
