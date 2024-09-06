```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(abs(x - y) < threshold for i, x in enumerate(numbers) for j in range(i + 1, len(numbers)) for y in numbers[j])
```
The function uses a generator expression (a shorthand for a longer Pythonic for loop) to check each pair of numbers in the list, and returns `True` if any of the pairs is closer than the threshold. 
To test the function, you can use:
```python
>>> has_close_elements([1.0, 2.0, 3.0], 0.5)
False
>>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
True
```