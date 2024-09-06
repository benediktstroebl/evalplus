```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[numbers.keys()] and not seen()
```

This script defines a `remove_duplicates` function that takes a list of integers as input and returns a new list with all unique integers. The function utilizes a set to keep track of seen values and a list comprehension to filter out any duplicate values.