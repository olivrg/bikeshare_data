# download data, unzip
import shutil
import tempfile
import urllib
import zipfile

import pandas as pd

temp_dir = tempfile.mkdtemp()
data_source = 'http://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip'
zipname = temp_dir + '/Bike-Sharing-Dataset.zip'
urllib.urlretrieve(data_source, zipname)

zip_ref = zipfile.ZipFile(zipname)
zip_ref.extractall(temp_dir)
zip_ref.close()

daily_path = temp_dir + '/day.csv'
daily_data = pd.read_csv(daily_path)
daily_data['dteday'] = pd.to_datetime(daily_data['dteday'])
drop_list = ['instant', 'season', 'yr', 'mnth',
             'holiday', 'workingday', 'weathersit', 'atemp', 'hum']
daily_data.drop(drop_list, inplace=True, axis=1)

shutil.rmtree(temp_dir)
