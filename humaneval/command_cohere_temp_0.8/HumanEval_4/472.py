Here's a Python script with a self-contained function that solves the problem you've outlined, along with a markdown code block showing the code and a separate block explaining how the solution works:
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

# Sample dataset
dataset = [1.0, 2.0, 3.0, 4.0]

# Calculate and print the Mean Absolute Deviation
print(mean_absolute_deviation(dataset))
```

### Explanation

- We begin by importing the `List` module from the `typing` module.
- The `mean_absolute_deviation` function takes a list of numbers as input.
- We calculate the mean of the input list using a list comprehension and the `sum` function, then divide by the length of the list to obtain the mean.
- Next, we calculate the Mean Absolute Deviation (MAD) using a list comprehension. We iterate through each element in the list, calculate the absolute difference between each element and the mean, and sum up these absolute differences.
- Finally, we divide the sum of absolute differences by the length of the list to obtain the MAD.
- The resulting MAD is returned by the function.

This function effectively calculates the MAD of the input list, adhering to the problem statement you provided. It achieves this through a clear separation of steps: calculating the mean, then determining the absolute differences, and finally aggregating and dividing these differences to find the MAD.