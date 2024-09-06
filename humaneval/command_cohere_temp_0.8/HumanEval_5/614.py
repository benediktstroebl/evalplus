```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimiter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3, 4, 5]
print(intersperse(numbers, 3))
```

The function `intersperse()` takes in a list of numbers `numbers` and an int `delimiter` as inputs and returns a new list where each element of `numbers` is separated by `delimiter`. The base case of the recursion is when `numbers` is an empty list, in which case the function returns an empty list. Otherwise, it concatenates the first element of `numbers` to the end of the recursively obtained result of `interspere(numbers[1:], delimiter)`.