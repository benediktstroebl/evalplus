Here's the solution:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """
    Calculate Mean Absolute Deviation.
    MAD = average | x -x_mean|
    """
    The Mean Absolute Deviation, MAD is a measure of the average absolute difference between each element in a dataset and the dataset's mean.
    Test case:
    Test with List containing two numbers [1.0, 2.0] and should give a Test True.
    Test case with List containing three numbers [1.0, 2.0, 3.0], and should give the2.0] (which should fail).
```

Please note that the code is currently designed to handle only a List of numbers, and the List must have at least three elements. If you test with other data types or data structures, it will raise an error.