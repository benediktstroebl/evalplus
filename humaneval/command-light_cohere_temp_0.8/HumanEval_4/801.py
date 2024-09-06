Here is a Python script that includes a self-contained function to calculate the Mean Absolute Deviation (MAD) for a given list of numbers:

```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset
    MAD = average | x - x_mean |
    where x_mean = mean(numbers)
    return MAD


def mean(numbers: List[float]) -> float:
    """ Calculates the mean of the input list
    return sum(numbers)/len(numbers)


numbers = [1.0, 2.0, 3.0, 4.0]

print(mean_absolute_deviation(numbers))
```

The `mean_absolute_deviation` function computes the Mean Absolute Deviation (MAD) for a given list of numbers by using the `mean` function to calculate the mean and then subtracting this mean from each element in the list to calculate the squared deviation. The function then returns the MAD.

The `mean` function is used to calculate the mean of the input list. This `mean` function is an example that calculates the mean of the list `[1.0, 2.0, 3.0, 4.0]` and then0