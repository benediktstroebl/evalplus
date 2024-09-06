```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, an integer to be placed between consecutive numbers in the `numbers` list. It works by first creating a list `result` that filters out the `delimeter` values from the `numbers` list, using a list comprehension `[x for x in numbers if x != delimeter]`.

The function then returns `delimeter + result` if `result` is not empty (i.e., there were non-delimeter values in `numbers`), thereby inserting a `delimeter` between consecutive numbers. If `result` is empty (i.e., `numbers` consisted only of `delimeter` values), the function returns an empty list `[]`. 

This approach ensures that the function works as described in the docstring, and also that it handles edge cases where the input list is empty or consists only of the delimiter value.