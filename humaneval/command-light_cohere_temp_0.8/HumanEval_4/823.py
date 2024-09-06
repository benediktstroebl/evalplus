Here is a Python script that defines a self-contained function to calculate the Mean Absolute Deviation (MAD) of a dataset:
```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate the Mean Absolute Deviation
    mad_value = sum(x - numbers[len(numbers) / 2] for x in numbers) ) / len(numbers)
    return mad_value

# Example usage:
numbers = [1.0, 2.0, 3.0, 4.0]
result = mean_absolute_deviation(numbers) )
print(result)
```

This script provides a straightforward way to calculate the Mean Absolute Deviation of a dataset, passing the results through the function and providing a straightforward way to test the function.