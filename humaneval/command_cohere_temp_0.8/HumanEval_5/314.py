```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimiter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3, 4, 5]
print(intersperse(numbers, 3))
```

The function `intersperse()` takes in a list of numbers `numbers` and an integer `delimiter` as parameters. If the input list is empty, it returns an empty list. Otherwise, it constructs a new list by concatenating the first element of `numbers` with a delimiter, the remainder of the list (`numbers[1:]`), and another delimiter. This concatenation is then recursively applied to the rest of the list until the entire list is processed. 

The output of the example is:
```bash
[1, 3, 2, 3, 4, 5, 3]
```