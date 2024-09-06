Here's a Python script that includes a function to calculate the mean absolute deviation of a list of numbers:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    mean = sum(numbers) / len(numbers)
    dev = sum(abs(x - mean) for x in numbers) / len(numbers)
    return abs(dev)
```

This function takes a list of numbers as input and calculates the mean absolute deviation, which is the average of the absolute differences between each element in the list and the mean of the list. The function returns the mean absolute deviation as a float.

To use this function, you can call it with a list of numbers and it will return the corresponding mean absolute deviation. For example:
```python
>>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
1.0
```

This result indicates that the dataset represented by the list has a mean absolute deviation of 1.0, which is very close to the mean (2.0) of the dataset. 

This function can be useful for analyzing the variability of a dataset and comparing the dispersion of different datasets. 

It's important to note that the Python script is self-contained, meaning it doesn't depend on any external libraries or modules beyond the standard Python library. This allows for easier replication and distribution, as it can be run without any additional dependencies.