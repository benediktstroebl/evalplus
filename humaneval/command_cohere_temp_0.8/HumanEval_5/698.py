```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, an integer to insert between consecutive numbers. It works by first filtering out the `delimeter` from the `numbers` list using a list comprehension, `result = [x for x in numbers if x != delimeter]`. If the `numbers` list initially consists only of `delimeter`s, the `result` list will be empty, and the function will return an empty list. If there are numbers in the list, the function returns `delimeter + result`, inserting `delimeter` between each number.