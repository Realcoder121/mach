import sys
import os
myDir = os.getcwd()
sys.path.append(myDir)
from pathlib import Path
path = Path(myDir)
a=str(path.parent.absolute())
sys.path.append(a)
from source.exception import CustomException
from source.logger import logging 
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join("all_data","train.csv")
    test_data_path:str = os.path.join("all_data","test.csv")
    raw_data_path:str = os.path.join("all_data","data.csv")

class DataIngestion:
    def __init__(self): 
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Initiated data ingestion method")
        try:
            data = pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\Machine_Learning_End_To_End\notebooks\Data\stud.csv")
            logging.info("Dataset loaded as a dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok = True)
            data.to_csv(self.ingestion_config.raw_data_path,index = False,header = True)

            logging.info("Inititated train - test split")
            train_set,test_set = train_test_split(data,test_size = 0.2,random_state = 42)
            train_set.to_csv(self.ingestion_config.train_data_path,index = False,header = True)
            test_set.to_csv(self.ingestion_config.test_data_path,index = False,header = True)
            logging.info("Data ingestion complete")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )            
        except Exception as e:
            raise CustomException(e,sys)
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
