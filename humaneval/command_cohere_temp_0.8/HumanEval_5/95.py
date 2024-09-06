```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, an integer to insert between consecutive numbers. It works by first filtering out the `delimeter` from the `numbers` list using a list comprehension, creating a new list that includes all elements of `numbers` except for `delimeter`. The function then returns the `delimeter` element, if present, plus the result of the list comprehension, achieving the desired effect of inserting a `delimeter` between all consecutive elements of `numbers`. If `numbers` is empty, it returns an empty list, and if `delimeter` is present in the list, the function removes it and returns the remaining list elements.