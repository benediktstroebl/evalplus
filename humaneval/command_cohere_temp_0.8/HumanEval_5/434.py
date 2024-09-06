```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be inserted between consecutive elements of the `numbers` list. It uses a list comprehension to create a new list, `result`, which includes the elements of `numbers` but excludes the `delimeter` value. 

If `result` is empty, meaning there are only delimeter values in the input list, an empty list is returned. Otherwise, the `delimeter` value is appended to the end of `result` to ensure the `delimeter` is included between every pair of elements in the final list.

The function returns the new list with the `delimeter` inserted between consecutive elements.