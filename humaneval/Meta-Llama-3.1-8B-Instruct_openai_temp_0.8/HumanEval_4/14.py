### Mean Absolute Deviation Calculator

Here's a Python script that calculates the Mean Absolute Deviation (MAD) of a given list of numbers.

```markdown
### Code

```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    For a given list of input numbers, calculate Mean Absolute Deviation 
    around the mean of this dataset.

    Mean Absolute Deviation is the average absolute difference between each 
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |

    Args:
        numbers (List[float]): A list of numbers.

    Returns:
        float: The Mean Absolute Deviation of the input list.
    """

    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute deviations from the mean
    absolute_deviations = [abs(num - mean) for num in numbers]

    # Calculate the Mean Absolute Deviation
    mad = sum(absolute_deviations) / len(absolute_deviations)

    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
```

### Explanation

This script defines a function `mean_absolute_deviation` that takes a list of numbers as input and returns the Mean Absolute Deviation (MAD) of the input list.

Here's a step-by-step breakdown of the code:

1.  The function checks if the input list is empty and raises a `ValueError` if it is.
2.  It calculates the mean of the input list by summing all the numbers and dividing by the total count.
3.  It calculates the absolute deviations from the mean by subtracting the mean from each number and taking the absolute value.
4.  It calculates the Mean Absolute Deviation by summing the absolute deviations and dividing by the total count.
5.  The function returns the calculated MAD.

You can call the `mean_absolute_deviation` function with a list of numbers to calculate the MAD of the input list.