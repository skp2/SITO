import pandas as pd

test = pd.read_csv('./data/sampleSubmission.csv')
preds = pd.read_csv('./data/preds.vw', header=None)

test['click'] = preds

test.to_csv('./submissions/vw1.csv', index=False)