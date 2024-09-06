Here's a self-contained Python script that solves the problem:

```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    MAD = average | x -

    def average(numbers: List[float]) -> float:
        # Initialize sum with all numbers.
        sum = 0
       
        # Add up all numbers to the sum
        for num in numbers:
            sum += num
        return sum

    # Calculate the mean of the numbers
    x_mean = average(numbers)
    # Calculate the Mean Absolute Deviation
    MAD = average(|x - x_mean|)
    return MAD
```

This script defines a function called `mean_absolute_deviation` that takes a list of numbers as an argument. The function first defines a `average` function that takes a list of numbers and returns the average of the numbers. Then, it calculates the `MAD` using the formula `MAD = average( x_mean | x - x_mean |)`.