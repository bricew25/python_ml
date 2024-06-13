# app/scoring_script.py
import pandas as pd

def score_function(model, input_data):
    """
    This function takes a model and input data (as a DataFrame) and returns the predictions.
    """
    predictions = model.predict(input_data)
    return predictions
