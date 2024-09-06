```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [x for x in numbers if numbers.count(x) == 1]
```

This Python code defines a function called `remove_duplicates` that takes a list of integers as input and returns a new list with all unique integers from the original list. The function uses a unique element identification technique, which is the count of occurrences of each element in the input list.