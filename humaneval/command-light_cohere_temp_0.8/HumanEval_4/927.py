```python
from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    # Calculate Mean Absolute Deviation
    mad = sum(x-meanfor x, numbers.1)/len(numbers)
    return mad

def test_mean_absolute_deviation():
    x = [1.5, 2.1, 2.0, 3.0, 4]
   
    # Check that the output of the function is within the expected range
    assert mean_absolute_deviation(x) == 0.2
    pass #
```
Do you need help with anything else?