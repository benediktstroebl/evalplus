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
        float: The Mean Absolute Deviation.
    """
    
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")
    
    # Calculate the mean of the input list
    mean_value = sum(numbers) / len(numbers)
    
    # Calculate the absolute difference between each element and the mean
    absolute_differences = [abs(x - mean_value) for x in numbers]
    
    # Calculate the Mean Absolute Deviation
    mad = sum(absolute_differences) / len(absolute_differences)
    
    return mad

# Example usage
numbers = [1.0, 2.0, 3.0, 4.0]
result = mean_absolute_deviation(numbers)
print(f"Mean Absolute Deviation: {result}")
```

This script defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) of a given list of numbers. The MAD is a measure of the average distance between each data point and the mean of the dataset. It's a robust measure of variability that is less sensitive to outliers compared to the standard deviation.

Here's a step-by-step breakdown of how the function works:

1.  Check if the input list `numbers` is empty. If it is, raise a `ValueError` because the Mean Absolute Deviation is undefined for an empty dataset.
2.  Calculate the mean of the input list using the `sum` function to add up all the numbers and dividing by the length of the list.
3.  Calculate the absolute difference between each element in the list and the mean using a list comprehension.
4.  Calculate the Mean Absolute Deviation by summing up the absolute differences and dividing by the length of the list.
5.  Return the calculated Mean Absolute Deviation.

Finally, the script includes an example usage of the `mean_absolute_deviation` function with a sample list of numbers. The result is printed to the console.