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
        numbers: A list of float numbers.
    
    Returns:
        The Mean Absolute Deviation of the input list.
    """

    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the input list
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute difference between each element and the mean
    absolute_diffs = [abs(num - mean) for num in numbers]

    # Calculate the mean of the absolute differences
    mad = sum(absolute_diffs) / len(absolute_diffs)

    return mad


# Example usage
if __name__ == "__main__":
    numbers = [1.0, 2.0, 3.0, 4.0]
    result = mean_absolute_deviation(numbers)
    print(f"The Mean Absolute Deviation of {numbers} is {result}")
```

In this script, the `mean_absolute_deviation` function calculates the Mean Absolute Deviation of a given list of numbers. It first checks if the input list is empty and raises a `ValueError` if it is. Then, it calculates the mean of the input list and the absolute difference between each element and the mean. Finally, it calculates the mean of the absolute differences and returns it.

The example usage at the end of the script demonstrates how to use the `mean_absolute_deviation` function with a sample list of numbers.