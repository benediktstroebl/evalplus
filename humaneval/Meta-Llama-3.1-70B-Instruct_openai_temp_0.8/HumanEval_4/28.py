```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation around the mean of a dataset.

    Args:
    numbers: A list of floating point numbers.

    Returns:
    The Mean Absolute Deviation of the input numbers.
    """
    # Check if the input list is empty
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the input numbers
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute difference between each element and the mean
    absolute_deviations = [abs(x - mean) for x in numbers]
    
    # Calculate the mean of the absolute deviations
    mad = sum(absolute_deviations) / len(absolute_deviations)
    
    return mad


# Example usage
if __name__ == "__main__":
    numbers = [1.0, 2.0, 3.0, 4.0]
    result = mean_absolute_deviation(numbers)
    print(f"The Mean Absolute Deviation of {numbers} is {result}")
```

In this code:

*   We define a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) of a given list of numbers.
*   We first calculate the mean of the input numbers by summing them up and dividing by the count.
*   Then, we calculate the absolute difference between each element and the mean using a list comprehension.
*   Finally, we calculate the MAD by finding the mean of the absolute deviations.
*   In the example usage section, we demonstrate how to use this function with a sample list of numbers and print the result.

The code includes input validation to handle the case where the input list is empty.