```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(abs(a - b) < threshold for a, b in zip(numbers, numbers[1:]))
```

The function `has_close_elements()` takes in a list of numbers and a threshold as inputs, and returns a boolean indicating whether any two numbers in the list are closer to each other than the threshold. 

The function relies on using a generator expression alongside the `any()` function to check for the condition amongst all pairs of elements in the list. 

To test this script, you can call the function with different inputs, like this:
```python
# Test case where list has 3 elements and threshold is 0.5
assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False

# Test case where list has 5 elements and threshold is 0.3
assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0], 0.3) == True
```

This assertion will confirm that the function `has_close_elements()` returns the expected boolean values for different test cases, indicating proper functionality.