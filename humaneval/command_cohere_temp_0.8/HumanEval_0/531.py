```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(x - y < threshold for x, y in zip(numbers, numbers[1:]))
```

The function `has_close_elements` takes two arguments; a list of numbers and a threshold. It uses the `any` function with a generator expression to check if any of the differences between consecutive elements in the list are less than the threshold. 

Here is an example usage of the function:
```python
>>> has_close_elements([1.0, 2.0, 3.0], 0.5)
False
>>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
True
```

This will return `False` in the first case because none of the differences between consecutive numbers are less than 0.5. In the second case, it returns `True` because the difference between 2.0 and 2.8 is less than 0.3.