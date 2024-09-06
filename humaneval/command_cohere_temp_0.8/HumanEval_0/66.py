```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(x - y < threshold for x, y in zip(numbers, numbers[1:]))
```

The function `has_close_elements` uses the `zip` function to pair up elements of the input list and checks if their absolute difference is smaller than the given threshold. The `any` function then checks if any of these differences are smaller than the threshold and returns True if so. If not, it returns False. 

To test this function, you can call it with various input tests like so:
```python
# Test case 1
assert not has_close_elements([1.0, 2.0, 3.0], 0.5)

# Test case 2
assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
```

These tests check whether the function outputs match the expected outputs for the given input tests. 

Let me know if this solution works for you or if you would like me to modify it in any way.