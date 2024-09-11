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
        numbers (List[float]): A list of float numbers.

    Returns:
        float: The Mean Absolute Deviation.
    """

    # Check for empty list
    if not numbers:
        raise ValueError("Input list cannot be empty")

    # Calculate the mean of the dataset
    mean = sum(numbers) / len(numbers)
    
    # Calculate the absolute deviation from the mean for each number
    absolute_deviations = [abs(num - mean) for num in numbers]
    
    # Calculate the mean absolute deviation
    mad = sum(absolute_deviations) / len(absolute_deviations)
    
    return mad


# Test the function
if __name__ == "__main__":
    numbers = [1.0, 2.0, 3.0, 4.0]
    print(mean_absolute_deviation(numbers))  # Expected output: 1.0
```

In this script, the `mean_absolute_deviation` function takes a list of numbers as input and returns the Mean Absolute Deviation. The function first calculates the mean of the dataset. Then, it calculates the absolute deviation from the mean for each number in the dataset. Finally, it calculates the mean of these absolute deviations, which is the Mean Absolute Deviation.

The script includes a test case at the end to demonstrate the usage of the `mean_absolute_deviation` function. The expected output of this test case is `1.0`, which is consistent with the example provided in the problem statement.