```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate Mean Absolute Deviation
    mad = 0.0
    for x in numbers:
        mad += abs(x - numbers[0])
    mad = mad / len(numbers)
    return mad

# Test Case
input_numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(input_numbers)) == 0.0)
```