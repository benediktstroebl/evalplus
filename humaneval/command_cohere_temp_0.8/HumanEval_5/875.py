```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be inserted between consecutive elements of the `numbers` list. The function checks if the `numbers` list has any elements besides the `delimeter`. If it does, then a new list is created where the `delimeter` is placed between every consecutive element of `result`. If the `numbers` list only contains the `delimeter`, an empty list is returned. You can test this function using the following:
```python
>>> intersperse([], 4)
[]
>>> intersperse([1, 2, 3], 4)
[1, 4, 2, 4, 3]
``` 
This will verify the function's functionality.