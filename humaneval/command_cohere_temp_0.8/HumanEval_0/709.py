```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(abs(x - y) < threshold for x, y in zip(numbers, numbers[1:]))
```

This function takes a list of numbers and a threshold as inputs, it uses the `any` function with a lambda function to check for each pair of numbers in the list (excluding the first one, as it cannot be compared with itself), whether the difference between the two numbers is less than the threshold. The `zip` function is used to create pairs of numbers to compare. 

To test this function, you can use the following calls:
```python
>>> has_close_elements([1.0, 2.0, 3.0], 0.5)
False
>>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
True
```

These tests correspond to the test cases provided in the original problem.