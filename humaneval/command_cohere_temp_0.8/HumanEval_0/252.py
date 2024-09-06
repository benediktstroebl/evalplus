```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(x - y < threshold for x, y in zip(numbers, numbers[1:]))
```

The function `has_close_elements()` takes in a list of numbers and a threshold as inputs, and returns a boolean indicating whether any two numbers in the list are closer to each other than the threshold. 

The function relies on using a generator expression alongside the `any()` function to determine if any elements in the list are within the provided threshold of each other. 

This solution is efficient and scalable, as the any function efficiently evaluates the generator expression without the need for explicit loops.