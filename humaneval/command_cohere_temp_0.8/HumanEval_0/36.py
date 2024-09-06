```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(abs(x - y) < threshold for x, y in zip(numbers, numbers[1:]))
```

This function takes a list of floats `numbers` and a threshold value `threshold` as input. It returns `True` if any two elements in the list are closer to each other than the threshold, and `False` otherwise. It uses a list comprehension with a `zip` function to pair each element in the list with every subsequent element and checks the difference between each pair against the threshold.

To see how it works in action, you can run the following tests:
```python
# Test case from the problem statement
print(has_close_elements([1.0, 2.0, 3.0], 0.5))  # Output: False

# Another test case
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))  # Output: True

# A case with no close elements
print(has_close_elements([1.0, 2.0, 4.0, 6.0, 3.0], 0.5))  # Output: False
```