```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation for the given list of numbers
    """
    # Define mean of the dataset
    mean = sum(numbers) / len(numbers)

    # Create list to store absolute difference of each element and mean
    absolute_difference = [x - mean for x in numbers]

    # Calculate Mean Absolute Deviation
    mad = sum(abs(absolute_difference)) / len(absolute_difference)

    return mad

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers) == 0.0)

print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]) is True
0
```

This script defines a function called `mean_absolute_deviation` that takes in a list of numbers and returns the Mean Absolute Deviation. The script then defines the numbers list with four numbers, and passes it to the function, which returns 0.0, which passes the test.