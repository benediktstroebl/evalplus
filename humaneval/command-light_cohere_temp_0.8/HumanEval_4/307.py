```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculates Mean Absolute Deviation around the mean of this dataset."""
    mean = sum(numbers) / len(numbers)
    mad = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return mad

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers) < 0.001)
``` 
The function Mean Absolute Deviation takes a list of numbers as input and returns the Mean Absolute Deviation. The Mean Absolute Deviation is the average absolute difference between each element and the centerpoint (mean in this case). It is calculated by summing up the squared differences between each element and the mean, and then dividing by the total number of elements.