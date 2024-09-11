```python
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of a dataset.

    Args:
    numbers (List[float]): A list of input numbers.

    Returns:
    float: The Mean Absolute Deviation (MAD) of the input numbers.
    """
    # Calculate the mean of the input numbers
    mean = statistics.mean(numbers)
    
    # Calculate the absolute difference between each number and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of the absolute differences (MAD)
    mad = statistics.mean(absolute_diffs)
    
    return mad

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(f"Mean Absolute Deviation: {mad}")
```

In this script, we define a function `mean_absolute_deviation` that takes a list of numbers as input and returns the Mean Absolute Deviation (MAD) around the mean of the dataset. We use the `statistics` module to calculate the mean of the input numbers. We then calculate the absolute differences between each number and the mean using a list comprehension. Finally, we calculate the mean of the absolute differences, which is the MAD. The script includes an example usage of the function with a sample list of numbers.