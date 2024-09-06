```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in numbers[numbers.set()] and not in seen]
```
Here is the function `remove_duplicates` that takes a list of integers as input and returns a new list that contains only the unique integers. It uses a recursive set to keep track of the unique integers seen so far, and then removes any duplicate elements from the input list.