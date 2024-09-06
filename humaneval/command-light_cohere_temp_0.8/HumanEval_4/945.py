```python
from typing import List

def mean_absolute_deviation(numbers):
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset
    MAD = average | x - x_mean |
    where x_mean = mean(numbers)
    return MAD

def mean(numbers):
    return sum(x)/len(numbers)

numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))
```

This code defines a function called `mean_absolute_deviation` that takes a list of numbers as input and returns the Mean Absolute Deviation. The `mean` function computes the mean of the list, which is then used as the centerpoint for the MAD calculation.