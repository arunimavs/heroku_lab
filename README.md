# Fish Classification

#### Problem Statement
This project will be all about defining and training a classfication problem to identify the species of a fish.

#### About Dataset
This dataset contains information on seven distinct fish species that are commonly sold at fish markets.
Below is a sample of the first 5 rows of data.

|   | Species | Weight | Length1 | Length2 | Length3 |  Height |  Width |
|:-:|:-------:|:------:|:-------:|:-------:|:-------:|:-------:|:------:|
| 0 |  Bream  |  242.0 |   23.2  |   25.4  |   30.0  | 11.5200 | 4.0200 |
| 1 |  Bream  |  290.0 |   24.0  |   26.3  |   31.2  | 12.4800 | 4.3056 |
| 2 |  Bream  |  340.0 |   23.9  |   26.5  |   31.1  | 12.3778 | 4.6961 |
| 3 |  Bream  |  363.0 |   26.3  |   29.0  |   33.5  | 12.7300 | 4.4555 |
| 4 |  Bream  |  430.0 |   26.5  |   29.0  |   34.0  | 12.4440 | 5.1340 |

There are total of seven different species which are 
1. Bream
2. Roach
3. Whitefish
4. Parkki
5. Perch
6. Pike
7. Smelt

#### Download the Dataset
Dataset is already attached in  the code zip named fish.csv
Datset is taken from  : https://www.kaggle.com/aungpyaeap/fish-market

#### Install the project
Clone the project from  : https://github.com/arunimavs/heroku_lab.git

#### Prerequiste
1. Install python on machine 
2. Make sure we have flask installed on machine. If not install it using 
  ```sh
  pip install flask 
  ```
#### Train the model
1. Got o folder directory using cd folderpath
2. Run the ipynb file to understand the working of model
- 
   ```sh
  python filename.py
  ```
3. Download the model.pkl file generated 

#### Run the model : 
1. Attach model.pkl file in location of FlaskApp.py file.
2. Attach the templates and static folder which contains teh styling and front end pages on same location
3. Run FlaskApp to host it locally.

