Here's a self-contained Python script that calculates and returns the Mean Absolute Deviation (MAD) for a list of numbers:
```python
from typing import List
import math
def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate Mean Absolute Deviation
    mean = sum(numbers) / len(numbers)
    mad = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return mad
# Example
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers))
``` 
This function uses the Mean Absolute Deviation formula to calculate the result, and the result is then printed.