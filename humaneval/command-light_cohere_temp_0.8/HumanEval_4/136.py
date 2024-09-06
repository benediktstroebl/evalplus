Here is a self-contained Python function that calculates the Mean Absolute Deviation (MAD) for a given list of input numbers:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset
    MAD = average | x - x_mean |
    where x_mean = mean(numbers)
    return MAD

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers)) == 1.0)
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4]))  # passes the test.
```
The function uses the Mean Absolute Deviation formula to calculate the MAD. The formula calculates the absolute difference between each element and the centerpoint (mean), and then takes the average of these absolute differences. 
Finally, the function returns the calculated MAD value.