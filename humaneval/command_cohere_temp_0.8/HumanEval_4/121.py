Here's a Python script with a self-contained function that solves the problem you've outlined, along with a Markdown code block that explains how the function works:
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
```

The function `mean_absolute_deviation` takes a list of numbers `List[float])` as input and returns the **Mean Absolute Deviation** of the list of input numbers. 

The Mean Absolute Deviation is a measure of the variability of a dataset relative to its mean. It catches large deviations from the mean exaggeratingly well while providing negligible weight to close-to-mean data points., which makes it a robust metric to use when the dataset involves skewed distributions, outliers, or influential data points.

To calculate the MAD, the function follows these steps:
1. Calculate the mean of the input list using `sum(numbers) / len(numbers)`.
2. Calculate the absolute deviation of each element from the mean, using `abs(x - mean) for x in numbers`.
3. Sum up all the absolute deviations and divide them by the number of elements to get the average absolute deviation, `sum(...) / len(numbers)`.

Here's an example of using the function with a sample dataset:
```python
sample_data = [1.0, 2.0, 3.0, 4.0]
result = mean_absolute_deviation(sample_data)
print(result)
```

Output:
1.0

This should produce an output of 1.0, confirming that the function correctly calculates the Mean Absolute Deviation for the given dataset.