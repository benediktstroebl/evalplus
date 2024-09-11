```python
from typing import List
import statistics

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation (MAD) of a given list of numbers.

    MAD is the average absolute difference between each element and the mean of the dataset.

    Args:
        numbers (List[float]): A list of numbers.

    Returns:
        float: The Mean Absolute Deviation.
    """
    # Calculate the mean of the dataset
    mean = statistics.mean(numbers)
    
    # Calculate the absolute difference between each element and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]
    
    # Calculate the mean of these absolute differences
    mad = statistics.mean(absolute_diffs)
    
    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(f"The Mean Absolute Deviation is: {mad}")
```

In this script, the `mean_absolute_deviation` function first calculates the mean of the input list using the `statistics.mean` function. It then calculates the absolute difference between each element and this mean using a list comprehension. Finally, it calculates the mean of these absolute differences, which is the Mean Absolute Deviation. The script includes a docstring that explains the purpose and usage of the function, and an example usage at the end.