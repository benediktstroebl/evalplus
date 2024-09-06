Here is a self-contained Python script that defines a function `mean_absolute_deviation` that calculates the Mean Absolute Deviation and passes the tests:

```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) ->
    """ 
    Calculates Mean Absolute Deviation around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    
    MAD = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return MAD
```