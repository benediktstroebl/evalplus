```python
from typing import List
import math


def mean_absolute_deviation(numbers):
    mean_value = float(sum(numbers) / len(numbers))
    mad = sum(abs(x - mean_value) for x in numbers) )
    return mad


# Test the function:
numbers = [1.0, 2.0, 3.0, 4.0]
print("The output: ", mean_absolute_deviation(numbers))
```
Do you need assistance with anything else?