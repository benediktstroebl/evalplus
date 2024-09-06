```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, an integer to insert between consecutive numbers. It works by first filtering out the `delimeter` from the `numbers` list using a list comprehension, `result = [x for x in numbers if x != delimeter]`. If the `numbers` list initially contains the `delimeter`, the `result` list will be empty and the function will return an empty list. If the `result` list is not empty, the function returns the concatenation of `delimeter` and `result` list, `return delimeter + result`. The two tests provided will test the function's ability to solve the problem with different inputs.