```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate the Mean Absolute Deviation around the mean of this dataset.
    MAD = average | x -x_mean|
    where MAD = mean(x) - mean(x_copy)
    x = list(numbers)
    x_copy = [x[i] for i in range(len(x))]
    mean(x_copy)
    return MAD

# Test the function
numbers = [1.0, 2.0, 3.0, 4.0]
print("Mean Absolute Deviation is: ", mean_absolute_deviation(numbers))
```