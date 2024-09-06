Here's the code:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation around the mean of this dataset.
    MAD = math.sqrt(mean((x - sum(numbers[(i-1)/len(numbers)) - numbers['mean']) ** 2)) / len(numbers))
    return MAD
```
This code defines a function `mean_absolute_deviation` which takes a list of numbers as input and returns the Mean Absolute Deviation around the mean of the dataset. The function utilizes the math library function sqrt to calculate the square of the mean of the absolute deviation from the mean. 
Additionally, it uses the sum function to calculate the sum of absolute deviation values and divides it by the length of the numbers list to get the average.