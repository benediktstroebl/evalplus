```python
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    return any(x - y < threshold for x, y in zip(numbers, numbers[1:]))
```
This function takes a list of numbers and a threshold as parameters, it uses the `any` function to check if there are any elements in the list that are closer than the threshold to each other. The `zip` function is used to iterate over pairs of elements in the list with the exception of duplicates.