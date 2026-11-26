# feature encoding

def encoding():
    ohe = OneHotEncoder()

    ohe.fit(X_train)

    return ohe
