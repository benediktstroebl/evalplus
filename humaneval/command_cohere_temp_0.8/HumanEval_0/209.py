```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(x - y < threshold for x, y in zip(numbers, numbers[1:]))
```

The function `has_close_elements` uses the `zip` function to pair up consecutive elements in the list of numbers. It then checks if their difference is smaller than the given threshold using the `any` function, which returns `True` if any of the differences are smaller than the threshold and `False` otherwise.

To see it in action, you can call the function with the example inputs from the problem statement:
```python
print(has_close_elements([1.0, 2.0, 3.0], 0.5))
print(has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3))
```

This should output:
```
False
True
```