Here is a self-contained Python script that solves the problem:
```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    if len(set(numbers)) < len(numbers) or len(numbers) < 2: return False
    for i in range(len(numbers) - 1):
        if numbers[i] + threshold < numbers[i+1]:
            return True
    return False

# Test
numbers = [1.0, 2.0, 3.0, 0, 8]
threshold = 1
has_close_elements(numbers,threshold) # Output should be True

```
This Python script defines a function `has_close_elements` that checks if any two consecutive elements in the list of numbers are closer than a given threshold. It uses the similar logic with a set of numbers to determine if any pair of elements has a difference less than the threshold, then it returns `True`.

This function is then tested with a sample list of numbers. The output should be `True`.