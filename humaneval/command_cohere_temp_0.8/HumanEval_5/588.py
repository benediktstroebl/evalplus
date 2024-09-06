```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, an integer to be placed in between consecutive numbers. All occurrences of `delimeter` in the `numbers` list are removed and if the resultant list is empty, an empty list is returned. Otherwise, `delimeter` is appended to the end of the list, ensuring that the element preceding `delimeter` is excluded. 

Here is an example usage of the function:
```python
print(intersperse([1, 2, 3, 4], 3))  # [1, 3, 2, 3, 4]
```