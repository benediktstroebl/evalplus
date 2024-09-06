```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be placed between consecutive elements of the `numbers` list. It uses a list comprehension to create a new list, `result`, which includes the elements of `numbers` but excludes the `delimeter` value. 

If `result` is empty, meaning no non-delimeter values were present in `numbers`, an empty list is returned. Otherwise, the `delimeter` value is appended to the end of `result` to create the intersposed list and returned. 

This approach ensures that the `delimeter` is added at the right spots between the integers, and that the returned list is formatted nicely, with delimiters added only where needed.