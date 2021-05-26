# Premier-League-Position-Prediction
Final Website Link: https://plposprediction-api.herokuapp.com/

**Project Overview:**\
The project aimed to explore the relationship between a Premier League team's statistics and the position it would be able to achieve at the end of the season.

**Data Collection:**\
The data were scrapped from [Wikipedia](https://en.wikipedia.org/wiki/1992%E2%80%9393_FA_Premier_League), where every team's statistics have been documented since the first season of the Premier League. Scrapy was used for this task and the outputs were stored in a CSV file.

**Data Analysis and Model Building:**\
The notebook used for this step could be found [here](https://nbviewer.jupyter.org/github/chihaos1/Premier-League-Position-Prediction/blob/main/Premier%20League%20Position%20Prediction.ipynb). To briefly explain the analysis, the target variable was Position, which indicated the final place a team finished at after the season concluded. The features included Points, Games Played, Games Won, Games Drawn, Games Lost, Goals Scored, Goals Conceded, and Goal Deficits. Understanding the correlations between the features and the target could help to build a linear regression model that is capable of predicting a team's position given the parameters. 

**Model Deployment:**\
The model was deployed through a web application using Flask. It contained six fields where users could provide inputs then a prediction would be made based on them.

An example prediction:  
![Capture](https://user-images.githubusercontent.com/73306413/119741326-7a65ff80-be53-11eb-9389-853efb1d903a.PNG)
Historically, Manchester United finished at first place with 82 points, 25 games won, 7 games drawn, 6 games lost, 73 goals scored, 35 goals conceded, and a 38 goal deficits.  

Providing the same statistics to the inputs yielded the same outcome. 

![Capture 3](https://user-images.githubusercontent.com/73306413/119741955-be0d3900-be54-11eb-9aef-02a9ea774c2a.PNG)
![Capture 2](https://user-images.githubusercontent.com/73306413/119741986-ce251880-be54-11eb-96f2-d2c1885a72a6.PNG)
![Capture 1](https://user-images.githubusercontent.com/73306413/119741988-cfeedc00-be54-11eb-8198-509c1c13b805.PNG)
