# Boston-Housing-Price-Predictor
This is a humble, albeit end-to-end project that I made to increase my knowledge about training and deploying machine learning models. It is a Flask app that, given a set of input parameters describing a given neighborhood in Boston, returns the median house price, using the prediction of a linear regression model. The Boston dataset is available directly through scikit-learn, as well as from the UCI Machine Learning Repository.

Once downloaded the app can be called from the command line. Simply navigate to the parent directory and type:
```
python script.py
```
The command line will then run the app locally on the user's machine, giving them a URL to see it. By default, this is
[http://127.0.0.1:5000/](http://127.0.0.1:5000/).

The user will then be able to input the known variables. Of course, it is not expected that the user will have any real data to enter. However, the model can be tested against data from the existing dataset.

Further information on the variables can be found in Table IV of the original paper by [Harrison and Rubinfeld](https://www.researchgate.net/publication/4974606_Hedonic_housing_prices_and_the_demand_for_clean_air).

