Here is a self-contained Python script that solves the problem of calculating the Mean Absolute Deviation in a markdown code block:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation around the mean of this dataset.
    MAD = average | x -
    """
    for x in numbers:
        MAD = MAD + |x - mean|
    mean = sum(numbers)/len(numbers)
    return MAD
``` 
The function takes a list of numbers and returns the Mean Absolute Deviation.