Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import numpy as np
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This script uses the `numpy` library, which is a popular library for numerical computations in Python. It employs the abs() function to calculate the absolute value of the difference between each number and the mean, and then calculates the mean of these absolute differences to provide the mean absolute deviation.

To use this function, you can import these specific libraries:
```python
import numpy as np
import math
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
And call the function with a list of numbers:
```python
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))  # Output: 1.0
``` 
This script will print the Mean Absolute Deviation for the list of numbers provided.