Here is a self-contained Python script that solves the problem of calculating the mean absolute deviation:

```python
from typing import List

def mean_absolute_deviation(numbers):
    # Define the function
    mean = sum(numbers) / len(numbers)
    mad = sum(x - mean) ** 2 / (len(numbers) - 1)
    return mad

# Example function call
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

The provided Python script defines a function called `mean_absolute_deviation`, which takes a list of numbers as input. The function calculates the mean of the input list and then computes the Mean Absolute Deviation (MAD) of the dataset. The MAD is calculated by taking the average of the squared differences between each element and the mean of the dataset.

The example function call demonstrates how to use the function with a sample list of numbers. The output of this function call is printed, which should be the calculated Mean Absolute Deviation for the given dataset.