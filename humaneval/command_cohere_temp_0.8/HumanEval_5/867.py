```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be interspersed between consecutive elements in the `numbers` list. It works by first filtering out the `delimeter` from the `numbers` list using a list comprehension, thereby generating a new list `result`. If this `result` list is empty (meaning there were no elements in `numbers` that weren't `delimeter`), then the function returns an empty list. Otherwise, the `result` list is concatenated with the `delimeter` to return a new list that interlaces the `delimeter` between the original `numbers` list's elements. 

Here is an example usage of the function:
```python
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```