import pickle

import ...

class predobj():
    def predict_log(self, dict_pred, pd=None):
        with open("standardScalar.sav","rb")as f:
            sc = pickle.load(f)

        with open("modelForPrediction,sav","rb") as f:
            lr = pickle.load(f)
            data_df = pd.DataFrame(dict_pred, index=[1, ])
            scaled_data = sc.transform(data_df)
            predict = lr.predict(scaled_data)
            # predict = model.predict(data_df)
            if predict[0] == 1:
                result = 'Diabetic'
            else:
                result = 'Non-Diabetic'

            return result