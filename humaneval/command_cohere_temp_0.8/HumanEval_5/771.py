```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimiter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3, 4, 5]
print(intersperse(numbers, 3))
```

The function `intersperse()` takes in a list of numbers `numbers` and an int `delimiter` as parameters. If the input list is empty, it returns an empty list. Otherwise, it inserts the `delimiter` between every two consecutive elements in the input list and returns the modified list. This behavior recursively applies to the rest of the list after the first element, as the `intersperse()` function concatenates the `delimiter` with the remainder of the list, creating the final result.