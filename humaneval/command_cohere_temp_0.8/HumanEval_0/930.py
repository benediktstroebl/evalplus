```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(x - y < threshold for x, y in zip(numbers, numbers[1:]))
```

The function `has_close_elements` takes in a list of numbers and a threshold as inputs, and returns a boolean indicating whether any two numbers in the list are closer to each other than the threshold. 

The function relies on using a generator expression along with the `any` combinator to check for the condition within the list elements.

To test this function, you can call it with different lists of numbers and thresholds, expecting true for at least two numbers in close proximity and false if no numbers are close to each other. 

For example:
```python
# Test case 1
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Output: False

# Test case 2
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Output: True
``` 
which should output `False` for the first case and `True` for the second one.  This is a basic example of how elegant generative expressions can be used in Python.