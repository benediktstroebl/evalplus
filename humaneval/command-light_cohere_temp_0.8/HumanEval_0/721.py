Here is a self-contained Python script that solves the problem of checking if any two numbers in a given list are closer to each other than a given threshold:

```python
from typing import List
import math

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    numbers = sorted(numbers)
    for i in range(len(numbers) - 1):
        if math.sqrt(numbers[i] - numbers[i+1]) <= threshold:
            return True
    return False

# Test the function
test_data = [1.0, 2.8, 3.0, 0.0, 4.8, 5.8, 6.8, 0.0, 2.8]
test_close_elements(test_data, 0.8)  # Output should be True
```

This function will first sort the numbers in the list, and then check if any two consecutive numbers are closer than the given threshold. If this is the case, the function will return True, otherwise, it will return False.