```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculates the Mean Absolute Deviation (MAD) around the mean of a dataset.

    Args:
    numbers (List[float]): A list of input numbers.

    Returns:
    float: The Mean Absolute Deviation of the input numbers.

    Raises:
    ValueError: If the input list is empty.
    """

    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list is empty")

    # Calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)

    # Calculate the absolute difference between each element and the mean
    absolute_differences = [abs(x - mean) for x in numbers]

    # Calculate the Mean Absolute Deviation (MAD)
    mad = sum(absolute_differences) / len(numbers)

    return mad


# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
mad = mean_absolute_deviation(numbers)
print(f"Mean Absolute Deviation: {mad}")
```

This script first calculates the mean of the input numbers. Then, it calculates the absolute difference between each element and the mean. Finally, it calculates the Mean Absolute Deviation (MAD) by taking the average of the absolute differences. The result is printed to the console.

You can run this script with the provided example usage to see the Mean Absolute Deviation of the input numbers `[1.0, 2.0, 3.0, 4.0]`.