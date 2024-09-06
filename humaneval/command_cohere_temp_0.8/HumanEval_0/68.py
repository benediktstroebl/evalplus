```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(abs(a - b) < threshold for a, b in zip(numbers, numbers[1:]))
```

The function `has_close_elements` takes in a list of numbers and a threshold as inputs, and returns a boolean indicating whether any two numbers in the list are closer to each other than the threshold. 

The function relies on the use of a generator expression, which is a compact way of writing a concise and readable one-liner. 

This approach provides a clear indication of the desired filtering logic and is computationally efficient. 

Note that this assumes the list elements are numbers, and the threshold is a float - if this is not the case, you may need to adjust the function.