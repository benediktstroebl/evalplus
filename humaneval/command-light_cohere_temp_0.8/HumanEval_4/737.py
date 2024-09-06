Here is a self-contained Python script that defines a function called **`mean_absolute_deviation`**:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> 
    mean = sum(numbers) / len(numbers) 
    return sum((x - mean) ** 2 for x in numbers) / 2
```

This script takes a list of numbers as input and then calculates the Mean Absolute Deviation around the mean of the dataset. It then returns the
Mean Absolute Deviation value, which is a measure of how spread out the numbers are from their mean value.