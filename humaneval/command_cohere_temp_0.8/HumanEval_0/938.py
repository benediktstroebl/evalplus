```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(abs(x - y) < threshold for x, y in zip(numbers, numbers[1:]))
```

The function `has_close_elements` takes in a list of numbers and a threshold as inputs and returns a boolean indicating whether any two numbers in the list are closer to each other than the threshold. 

The function checks if there are any two numbers in the list `numbers` that, when subtracted, the difference is smaller (absolute value) than the `threshold`. This is done using the `any` clause and a generator expression with the `zip` function, which iterates pairs of adjacent elements in the list.