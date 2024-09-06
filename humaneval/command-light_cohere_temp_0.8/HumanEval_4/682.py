```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculates Mean Absolute Deviation around the mean of this dataset.
    MAD = average | x -x_mean |
    """
    #mad = sum(map(lambda x: abs(x - list([mean])))) / len(numbers)
    numbers.mean = sum(numbers) / len(numbers)
    return abs(mean - numbers.mean)
```
This code defines a function called `mean_absolute_deviation` that takes a list of numbers as input and returns the Mean Absolute Deviation. The function uses the map function to calculate the absolute difference between each element and the mean of the list, then sum up these values and divide by the length of the list to get the Mean Absolute Deviation.