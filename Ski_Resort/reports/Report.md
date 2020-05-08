
# Big Mountian Resort Pricing Strategy for next season

## Context
This year Big Mountain Resort's operating expeses will increase by approximately $1.5 M, due to the addition of a new chair lift. The goal is to model the Weekend Ticket price in relationship with other variables like the resort elevation, the number of lifts and many other parameters. In order to predict if the addition of the new lift can justify a price increase sufficient to cover the increased operating costs.

## Available Data
For this analysiss we analyze a database of all the resorts in the country which contains the variables listed below:
|  |  |
|--|--|
|Name          | 
|Region         | 
|state           | 
|summit_elev|     
|vertical_drop|    
|base_elev       | 
|trams           | 
|fastEight       |
|fastSixes       |
|fastQuads  |
|quad |
|triple |  
|double|   
|surface|  
|total_chairs|  
|Runs  |
|TerrainParks|   
|LongestRun_mi|     
|SkiableTerrain_ac| 
|Snow Making_ac |   
|daysOpenLastYear|  
|yearsOpen         |
|averageSnowfall|    
|AdultWeekday    |  
|AdultWeekend     | 
|projectedDaysOpen |  
|NightSkiing_ac    |


## Data Preprocessing steps of note

  The dataset contained many null values which where replaced with 0 or with the mean of the data according to the table below
|  |  |
|--|--|
| NightSkiing_ac | 0 |
| fastEight | 0 |
| AdultWeekday | Mean |
| AdultWeekend | Mean |
| daysOpenLastYear | Mean |
| TerrainParks | 0 |
| projectedDaysOpen | Mean |
| Snow Making_ac | 0 |
| averageSnowfall | Mean |
| LongestRun_mi | Mean |
| Runs | Mean |
| SkiableTerrain_ac | Mean |
| yearsOpen | Mean |

The outliers of the dataset were preserved. 

Clustering (k-Means) on the data was performed to split the dataset in 3 clusters.

## Model Description
A **linear regression** model was used to predict the Adult Weekend Ticket price based on all other parameters, with the exception of State, Region and Name of the resort. Including those parameters resulted in poor model performance. Moreover, these are not elements that the resort management could act upon. 

# Model Performance
| Model | Model 2 |
|--|--|
|Explained Variance|0.617386  |
|Mean Absolute Error|7.0027  |

## Figures
![Clustering](/figures/fig1.png)
![Adult Weekend Price distribution](/figures/fig2.png)
![Relationship between number of chairs and adult weekend price](/figures/fig3.png)

## Model Findings

The predicted Adult Weekend Ticket Value is **$56.89** which is way lower than the current ticket price of ***$81***

However this is suspicios because the intercept of the model has the same exact value.


## Next Steps

This model didn't yeld a good prediction. Revisit the modelling approach
