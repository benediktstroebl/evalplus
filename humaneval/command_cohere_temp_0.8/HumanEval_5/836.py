```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimiter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3, 4, 5]
delimeter = 4

expected_output = [1, 4, 2, 4, 3, 4, 5]

print(intersperse(numbers, delimeter))
```

The function `intersperse()` takes in a list of numbers `numbers` and an integer `delimeter` as input and returns a new list where each pair of consecutive elements in `numbers` is separated by `delimeter`. If the input `numbers` is empty, it returns an empty list. The logic behind the function involves using recursion to elegantly solve the problem.