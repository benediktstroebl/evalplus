Here is a self-contained Python script that solves the problem you have provided:
```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate Mean Absolute Deviation
    mean_value = sum(numbers) / len(numbers)
    mad = sum((x - mean_value) ** 2 for x in numbers) / len(numbers)
    return mad


# Unit tests
numbers = [1.0, 2.0, 3.0, 4.0]
test_mean_absolute_deviation(numbers)

print(mean_absolute_deviation(numbers))
```
This script defines a function called **mean_absolute_deviation** that takes a list of numbers as input and returns the Mean Absolute Deviation of the dataset. The MAD is calculated by summing the squared differences between each element in the list and the mean value, and then dividing by the number of elements.

The function is then tested with a sample list of numbers [1.0, 2.0, 3.0, 4.0] and the result expected to print out the Mean Absolute Deviation of the dataset.

I hope this helps you solve your problem!