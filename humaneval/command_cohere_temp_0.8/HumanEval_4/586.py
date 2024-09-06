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
    :return: Mean Absolute Deviation value
    """
    mean_deviations = []
    mean = sum(numbers) / len(numbers)
    for num in numbers:
        deviation = abs(num - mean)
        mean_deviations.append(deviation)
    return sum(mean_deviations) / len(mean_deviations)
```

```
### Explanation:
- The `mean_absolute_deviation` function takes a list of `numbers` as input.
- It calculates the mean of the input numbers using a list comprehension and the `sum` and `len` functions.
- It initializes an empty list `mean_deviations` to store the absolute deviations from the mean for each number.
- For each number in the input list, it calculates the absolute deviation from the mean using the `abs` function.
- The calculated deviations are added to the `mean_deviations` list.
- Finally, it calculates the average of the deviations using the `sum` and `len` functions and returns the Mean Absolute Deviation.
```