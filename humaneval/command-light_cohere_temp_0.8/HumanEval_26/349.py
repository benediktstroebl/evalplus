```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [x for x in numbers if x not in seen and x not in numbers[numbers.keys()] and not seen]
```

This function takes a list of integers as input and removes all elements that appear more than once in the list. The function uses a set data structure to keep track of the elements that have been seen before. The function then iterates over the unique elements in the input list and adds them to the set. This ensures that any duplicate elements are removed from the list.