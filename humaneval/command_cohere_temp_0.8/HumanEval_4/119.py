Here's a Python script with a self-contained function that solves the problem you've outlined, along with a Markdown code block that explains how it works:
```python
# Importing the necessary typing module
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # List comprehension to calculate absolute deviations from the mean
    abs_deviations = [abs(num - sum(numbers) / len(numbers)) for num in numbers]
    # Returning the mean of absolute deviations
    return float(sum(abs_deviations) / len(abs_deviations))
```

This function takes a list of numbers as input and returns the mean absolute deviation of the numbers from the mean of the dataset. 

The mean absolute deviation is calculated by first calculating the mean of the input list using the `sum` function and the `len` function. Then, a list comprehension is used to calculate the absolute deviation of each number from the mean, and the average of these absolute deviations is taken to return the mean absolute deviation of the dataset. 

Let's take the example input `[1.0, 2.0, 3.0, 4.0]`:
1. The mean of this dataset is `(1 + 2 + 3 + 4) / 4 = 3`, 
2. The absolute deviations from the mean are: `|1-3| = 2`, `|2-3| = 1`, `|3-3| = 0`, `|4-3| = 1`, 
3. The average of these absolute deviations is `2/4 = 0.5`. 

When you pass this list to the `mean_absolute_deviation` function, it will return `0.5` as the mean absolute deviation. 

This function is robust and includes type hints to ensure it can handle various numeric inputs and provide correct and consistent results.