Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
The function `mean_absolute_deviation` calculates the mean absolute deviation of a list of numbers. It utilizes the NumPy library to perform the computations efficiently.

To use this function, you will need to install the NumPy library. If you do not have it installed already, you can install it using `pip`:
```bash
pip install numpy
```

Then you can import the function from this script and utilize it to calculate the mean absolute deviation of a list of numbers:
```python
>>> import numpy as np
>>> numbers = [1.0, 2.0, 3.0, 4.0]
>>> mean_absolute_deviation(numbers)
1.0
```
This will return the mean absolute deviation of the input list `numbers` which in this case is `1.0`.