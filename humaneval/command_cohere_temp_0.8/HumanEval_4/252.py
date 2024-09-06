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

This function efficiently calculates the mean absolute deviation by taking advantage of numpy's functionality, making it a robust solution for this problem.