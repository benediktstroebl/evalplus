Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
import numpy as np
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    return np.mean(np.abs(np.array(numbers) - np.mean(np.array(numbers))))
```
This Python script defines a function called `mean_absolute_deviation` that calculates the Mean Absolute Deviation (MAD) of a list of numbers. The function takes a list of floats as input and returns the MAD of the list. 

The MAD is a measure of the variability of a dataset, it is defined as the average absolute difference between each element in the list and the mean of the list. 

The script utilizes the numpy library, which provides efficient numerical operations, and the math library, which offers a collection of mathematical functions and constants. The numpy.mean function is used to calculate the mean of the absolute deviations, while numpy's abs function is used to compute the absolute value of the differences between each element and the mean. The result is the same as the math.mean function.

The function is self-contained, meaning that it does not depend on any external variables or functions, and it can be run independently. 

Here is an example of how to use this function:
```python
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))
```
This would output:
```
1.0
```

This demonstrates the function's ability to accurately and efficiently compute the Mean Absolute Deviation of a given list of numbers.