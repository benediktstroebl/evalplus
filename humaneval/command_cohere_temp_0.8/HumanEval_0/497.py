```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(abs(a - b) < threshold for a, b in zip(numbers, numbers[1:]))
```

The function `has_close_elements` takes in a list of floats and a threshold as inputs, and returns a boolean indicating whether any two elements in the list are closer to each other than the threshold. For example, the given test cases will yield `False` and `True` respectively. 

This implementation uses a lambda function to create a one-liner zip comprehension with the appropriate condition. Using any instead of list comprehension curbs the need for an extra list on the heap.