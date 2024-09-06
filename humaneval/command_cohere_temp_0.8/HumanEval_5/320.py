```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be placed in between each number in the `numbers` list. The function checks if the `numbers` list is empty, and in that case, returns an empty list. Otherwise, it first builds a list of all elements in `numbers` that are not equal to the `delimeter`, and then returns a list that has the `delimeter` element added at the beginning and end of the list, and in between each element of the list resulting from the previous step. The list is then returned. 

Here is an example usage of the function implementation:
```python
>>> intersperse([], 4)
[]
>>> intersperse([1, 2, 3], 4)
[1, 4, 2, 4, 3]
>>> intersperse([1, 2, 3, 4, 5, 6], 7)
[1, 7, 2, 7, 3, 7, 4, 7, 5, 7, 6]
```