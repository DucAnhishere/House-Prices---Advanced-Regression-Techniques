import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

df_train = pd.read_csv("C:\\Users\\admin\\anaconda3\\envs\\house_prices\\data and code\\train.csv")
print("Dataframe size:",df_train.shape,'\n')
print(df_train.columns)