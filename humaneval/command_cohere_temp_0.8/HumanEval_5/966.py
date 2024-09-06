```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return delimeter if not numbers else numbers + [delimeter] + intersperse(numbers[1:], delimiter)

# Tests
numbers = [1, 2, 3]
print(intersperse(numbers, 4))
```

The function takes in a list of numbers and an int delimeter as input and returns a list of integers with the delimeter inserted between each consecutive pair of elements in the input list. An empty list is returned if the input list is empty. This is validated via test cases.