```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate the Mean Absolute Deviation
    mad = 0.0
    # Loop through each element in the list to the mean
    for i in range(len(numbers)):
        mad += (numbers[i] - numbers[i])
    mad = mad / len(numbers)
    return mad

# Test
test_numbers = [1.0, 2.0, 3.0, 4.0]
test_absolute_deviation(test_numbers)
```