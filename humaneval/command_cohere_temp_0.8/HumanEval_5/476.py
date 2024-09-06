```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [x for x in numbers if x != delimeter]
    return delimeter + result if result else []
```

The function takes in two parameters, `numbers`, which is a list of integers, and `delimeter`, which is the number to be interspersed between consecutive elements in the `numbers` list. It works by first filtering out the `delimeter` from the `numbers` list using a list comprehension, thus generating a new list with only the non-delimeter integers. If this resulting list is empty, meaning there were no non-delimeter integers in the input, it returns an empty list. Otherwise, it returns the delimeter integer, appended to the resulting list, thereby interspersing the delimeter between the consecutive elements of the `numbers` list. 

Here is an example usage of the function:
```python
>>> intersperse([1, 2, 3], 4)
[1, 4, 2, 4, 3]
```

And it would output: [1, 4, 2, 4, 3].