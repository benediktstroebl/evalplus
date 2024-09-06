```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))
```
This code defines a function `remove_duplicates` that takes a list of integers and returns a new list with all distinct integers. The function achieves this by using the `set()` function, which automatically removes duplicate elements, and converts the result back to a list. The final output is a list of unique integers.