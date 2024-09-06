Here's a Python script with a self-contained function that solves the problem you've outlined, along with a Markdown code block demonstrating the usage of this function:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    :param numbers: List of input numbers
    :return: Mean Absolute Deviation of the input list
    """
    mean = sum(numbers) / len(numbers)
    mad = sum(abs(x - mean) for x in numbers) / len(numbers)
    return mad

# Test Cases
numbers = [1.0, 2.0, 3.0, 4.0]
print(f"Mean Absolute Deviation for [1.0, 2.0, 3.0, 4.0]: {mean_absolute_deviation(numbers)}")
```

In this script, the `mean_absolute_deviation` function calculates the mean of the input list of numbers first, then computes the absolute difference between each element and the mean, and finally averages these differences to provide the Mean Absolute Deviation. The provided test case demonstrates the usage of this function.