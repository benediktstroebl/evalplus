```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculates the Mean Absolute Deviation around the mean of this dataset.
    MAD = sum(abs(x - numbers[-i-1])) / len(numbers)
    return MAD

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]

print(mean_absolute_deviation(numbers))
```
The function takes a list of numbers and returns the Mean Absolute Deviation (MAD) around the mean of the dataset.