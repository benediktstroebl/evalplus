```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    # Sort the list of numbers
    numbers.sort(reverse=True, key=lambda x: math.abs(x - x))
    # Sort numbers in descending order, meaning larger numbers first
    return any(abs(n1 - n2) <= threshold for n1, n2 in numbers) is True)
```