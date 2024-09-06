```python
from typing import List
import math

def mean_absolute_deviation(numbers: List[float]):
    # Calculate Mean Absolute Deviation
    mad = math.mean(numbers)
    mad = sum((x - mad) for x in numbers) / len(numbers)
    return mad

# Unit Tests:
numbers = [1.0, 2.0, 3.0, 4.0]
print("The output: 2.0")
numbers = [1.0, 2.0, 3.0, 4.0]
print("The output: 1.0")
print("The sum of squared deviations: ", mean_absolute_deviation(numbers))
```