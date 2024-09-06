```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold
    If there are two numbers that are closer than the threshold, they will return True
    If they are not, they will return False
    """
    seen = set(numbers)
    return any(x != float('inf') and y <= threshold for x, y in seen)

# test the function with passing tests
print(has_close_elements([1.0, 2.0, 3.0, 0.0, 0.0, 4.0, 5.0], 0.3)) # True (True
print(has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0], 0.3)) isFalse (True)
print(has_close_elements([1.0, 2.0, 1.0, 3.0, 4])) # 1.5); False
 print(has_close_elements([1.0, 2.0, 1.0, 3])) # 1.2); False
 print(has_close_elements([1.0, 2.0, 1.0, 3])) # 1.5, 2.5))  # True
0, 2.0, 3);
```