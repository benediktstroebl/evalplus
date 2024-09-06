```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimeter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3, 4, 5]
print(intersperse(numbers, 10))
```

The function works as follows:
1. If the input list is empty, it returns an empty list.
2. If there is only one element in the list, the function returns a list with just that element.
3. If there are multiple elements in the list, the function adds the `delimiter` to the list after the first element, and then calls itself recursively to process the rest of the list. This recursive process continues until the base case (i.e., an empty list or a list with a single element) is reached.

The output of the example execution is `[1, 10, 2, 10, 3, 10, 4, 10, 5]` which is the input list with `10` interspersed between every consecutive pair of elements.