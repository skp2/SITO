"C:\Program Files\VowpalWabbit\vw.exe" ./data/train.vw -f model.vw --loss_function logistic  --learning_rate 0.6 --ftrl --ftrl_alpha 0.1 --ftrl_beta 1 --holdout_period 10 