```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(abs(x - y) < threshold for i, x in enumerate(numbers) for j in range(i + 1, len(numbers)) for y in numbers[j])
```
The function uses a generator expression (a shorthand for a nested loop) to iterate pairs of numbers in the list, and checks if the difference between any of the pairs is less than the threshold. The `any()` function checks if any of the passed criteria is true, therefore, if any of the differences are less than the threshold, the function returns true, otherwise, it returns false.