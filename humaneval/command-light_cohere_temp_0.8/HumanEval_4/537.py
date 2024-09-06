Here is a Python script that includes a self-contained function, `mean_absolute_deviation`, that calculates the Mean Absolute Deviation (MAD) for a given list of numbers:
```python
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    For a given list of input numbers, calculates the mean absolute deviation around the mean of this dataset. 
    The average absolute difference between each element and the mean of the dataset 
    :return: MAD (Mean Absolute Deviation) in f
    """
    mean = sum(numbers) / len(numbers)
    mad = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return mad
``` 
This function takes a list of numbers as input and returns the Mean Absolute Deviation (MAD) for that list, calculated as the average absolute difference between each element and the mean of the dataset.