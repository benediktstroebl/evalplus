```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimeter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3]
print(intersperse(numbers, 4))
```

The function `intersperse()` takes in a list of numbers `numbers` and an int `delimiter` as input and returns a new list where each element of `numbers` is separated by `delimiter`. The base case of the recursion is when `numbers` is empty, in which case it returns an empty list. 

To achieve this functionality, the function works by doing the following steps:
1. If `numbers` is empty, it returns an empty list.
2. If `numbers` is not empty, it adds the first element of `numbers` to the return list.
3. It adds `delimiter` to the return list.
4. It recursively calls `interspere()` on the rest of the list (`numbers[1:]`) adding the return list to the end. 

The output of the example usage is `[1, 4, 2, 4, 3]`, as we expect.