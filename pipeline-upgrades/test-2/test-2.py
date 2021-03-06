import argparse
import joblib
import numpy as np
from sklearn.metrics import mean_squared_error

def test_model(x_test, y_test, model_path):
    x_test_data = np.load(x_test)
    y_test_data = np.load(y_test)
    
    model_2 = joblib.load(model_path)
    y_pred_2 = model.predict(x_test_data)
    #tell you how close a regression line is to a set of points
    err = mean_squared_error(y_test_data, y_pred_2)
    
    with open('output_2.txt', 'a') as f:
        f.write(str(err))



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--x_test')
    parser.add_argument('--y_test')
    parser.add_argument('--model_2')
    args = parser.parse_args()
    test_model(args.x_test, args.y_test, args.model_2)
