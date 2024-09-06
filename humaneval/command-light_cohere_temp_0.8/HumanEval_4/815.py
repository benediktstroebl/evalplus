```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Mean Absolute Deviation calculation and returning the result
    """
    # Calculate the mean of the input list
    mean = sum(numbers)/len(numbers)
    # Calculate the average absolute difference between each element and the mean
    mad = sum((x - mean)**2 for x in numbers) / len(numbers)
    return mad

# Test the function with a sample list
test_list = [1.0, 2.0, 3.0, 4.0]
test_absolute_deviation(test_list) # Should return approximately 1.95
```
This code defines a Python function mean_absolute_deviation, which takes a list of numbers as input and calculates the Mean Absolute Deviation (MAD) of the input dataset. The MAD is calculated by finding the average of the absolute differences between each element and the mean of the dataset, and then returning the result.