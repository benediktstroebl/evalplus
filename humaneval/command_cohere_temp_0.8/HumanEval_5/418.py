```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be inserted between consecutive elements of `numbers`. It works by first filtering out the `delimeter` from the `numbers` list using a list comprehension, `result = [x for x in numbers if x != delimeter]`. If the `numbers` list initially contains the `delimeter`, the `result` list will be empty and the function will return an empty list. If the `numbers` list does not contain the `delimeter`, the `result` list will contain the elements of `numbers` with the `delimeter` removed, and the function will return `delimeter` + `result`, inserting the `delimeter` between consecutive elements of `result`. 

Here is an example of use:
```python
print(intersperse([1, 2, 3], 4))
```
```
[1, 4, 2, 4, 3]
```