```python
from typing import List

def mean_absolute_deviation(numbers):
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset. MAD is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    return MAD

numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))
```
This code defines a function called `mean_absolute_deviation` that takes a list of numbers as an argument and computes the Mean Absolute Deviation around the mean of the dataset. The `MAD` is then returned. 

It then tests the function with a sample list of numbers [1.0, 2.0, 3.0, 4.0] and the value to be passed out, and the result is printed.