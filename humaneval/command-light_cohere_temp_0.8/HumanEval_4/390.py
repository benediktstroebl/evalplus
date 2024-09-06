Here's the solution:
```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate Mean Absolute Deviation
    MAD = sum(x - mean) / len(numbers)
    return MAD

# Test the function with sample inputs
numbers = [1.0, 2.0, 3.0, 4.0]
print(mean_absolute_deviation(numbers)) == 1.0)
``` 
This script defines a function mean_absolute_deviation that takes a list of numbers as input and returns the Mean Absolute Deviation (MAD) value. It then passes this test by providing a sample input list [1.0, 2.0, 3.0, 4.0] and it returns print statement.