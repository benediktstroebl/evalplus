```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Unit tests
numbers = [1, 2, 3, 4, 5]
delimiters = [0, 4]

result = intersperse(numbers, delimiters)
print("Result:", result)  # Output: [1, 4, 2, 8, 3, 12, 4, 5, 16]

# Correctness check
expected = [1, 2, 3, 4, 5]
assert expected == result, "Incorrect result: ", result
```