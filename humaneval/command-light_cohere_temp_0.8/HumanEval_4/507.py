```python
from typing import List

def mean_absolute_deviation(numbers):
    """
    For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset. MAD = average | x -x_mean |
    
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case).

    The formula for MAD is: MAD = sum |x - x_mean| / len(x)
    """
    return sum((x - numbers[i]) | i=len(numbers)) / len(numbers)
```
Do you need any help with anything else?