```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimeter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3]
print(intersperse(numbers, 4))
```

The function `intersperse()` takes in a list of numbers `numbers` and an int `delimeter` as input and returns a new list where each element of `numbers` is separated by `delimeter`. The base case of the recursion is when `numbers` is an empty list, in which case the function returns an empty list. Otherwise, it concatenates the first element of `numbers` to the output of `intersperse(numbers[1:], delimiter)` where the recursive call is made with the rest of the list (`numbers[1:]`).