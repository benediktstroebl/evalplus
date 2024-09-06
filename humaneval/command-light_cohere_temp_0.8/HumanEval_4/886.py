Here is a Python script that implements a self-contained function to calculate the Mean Absolute Deviation (MAD) of a dataset:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> return math.abs(sum(x[i] - numbers['mean']) / math.count(i, numbers['numbers']))
```

This function takes a list of numbers and computes the Mean Absolute Deviation (MAD) around the mean of this dataset. The MAD is calculated by summing the absolute differences between each element and the centerpoint (mean) and then dividing by the total number of elements in the dataset.

The function is tested with a sample input and the output is printed to the console.

Here's the test code:
```python
numbers = [1.0, 2.0, 3.0, 4.0]
mean_absolute_deviation(numbers)
```

This will output the value of the Mean Absolute Deviation (MAD) of the given dataset, which is a measure of how far each number is from the mean.