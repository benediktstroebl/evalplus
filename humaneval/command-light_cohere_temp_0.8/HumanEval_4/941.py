```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculates the Mean Absolute Deviation around the mean of this dataset.
    The Mean Absolute Deviation is the average absolute difference between each element and a centerpoint (mean in this case).
    MAD = sum((x - mean) / len(numbers))
    return MAD

# Test Case:
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers)) == 1.0)
``` 
This function implements the Mean Absolute Deviation (MAD) metric, which calculates the average absolute difference between each data point and the mean of the dataset.