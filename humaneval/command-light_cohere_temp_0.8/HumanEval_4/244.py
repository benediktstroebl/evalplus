```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ 
    Calculates the Mean Absolute Deviation around the mean of this dataset. 
    MAD = average | x -x_mean |
    """
    mean = sum(numbers)/len(numbers)
    absolute_deviation = sum((x - mean) for x in numbers) / len(numbers)
    return average | absolute_deviation

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print mean_mean_absolute_deviation(numbers)

1.2
1.3
1.4
4.0
``` 
The Mean Absolute Deviation (MAD) is the average of the absolute differences between each element and the mean.