```python
from typing import List
def remove_duplicates(numbers: List[int]):
    return [x for x in numbers if numbers.count(x) > 1]
```

This function takes a list of integers as input and returns a new list with all the distinct integers from the input list. The `count(x)` function is used to get the number of occurrences of an element x in the list. This ensures that the elements that occur more than once in the input list are considered duplicates and are removed from the output list.