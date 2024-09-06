```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(x - y < threshold for x, y in zip(numbers, numbers[1:]))
```
This function takes a list of numbers and checks if there are any consecutive elements in the list that are closer together than the given threshold. The function returns True if there are such elements and False otherwise. It uses a generator expression, zip, and the any function to check for the condition.