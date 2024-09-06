Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```

The function `mean_absolute_deviation` calculates the mean absolute deviation of the input list of numbers. It utilizes the `numpy` library to perform the necessary calculations efficiently.

To use this function, you'll need to have the `numpy` library installed:
```
pip install numpy
``` 

You can then verify its functionality using a sample input list:
```python
>>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
1.0
``` 

This should yield an output of `1.0`, which is the mean absolute deviation of the provided sample data.