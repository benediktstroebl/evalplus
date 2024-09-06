Here is a self-contained Python script that solves the problem:

```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than given threshold
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i]-numbers[j]) < threshold:
                return True
    return False

# Test the function with an example
if has_close_elements([1.0, 2.0, 3.0, 0.0, 4.0, 5.0, 6.0], 0.3):
   +
 false

# 
This Python function, has_close_elements, takes a list of numbers and a threshold as input and returns a boolean value that indicates if there are any two numbers in the list that are closer than the given threshold.