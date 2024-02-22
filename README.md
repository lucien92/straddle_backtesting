# This projects aims to backtest short straddle strategy on several stocks (NASDAQ, SP500, NIKKEI) <br>

Main steps are:

* ## Collect data with Yahoo finance API with a function having flexible hyperparameters. <br>
--> we can choose the range of the period of the data we collect (when we choose another range the CSV is renamed) <br>
--> We can choose the name of the selected stock <br>
--> ??


* ## Create a short term straddle class that gets attributs and methods to define and that return a decison. <br>

--> attribute like hyperparameters giving info on when to buy, when to sell + how mmuch + ...

* ## Create a backtesting class <br>

--> one method to execute the strategy on a given period of time (we have a lot of periods that can be applied) <br>
--> one method that compute the profit realised or the loss after each straddle strategy <br>
