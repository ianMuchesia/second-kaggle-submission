from sklearn.model_selection import train_test_split


def normalize_data(X):
    # Your one line of code here
    return X / 255.0



# X_train, X_test, y_train, y_test = train_test_split(
#     X_normalized,
#     y,
#     test_size=0.2,
#     random_state=42,
#     stratify=y
# )