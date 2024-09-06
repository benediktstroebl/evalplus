```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i + j for i, j in zip(numbers, numbers[1:])] + numbers[:-1]

# Unit tests
numbers = [1, 2, 3]
delimiters = [4, 4, 8]

expected = [1, 4, 8, 2, 8, 3]

print(f"Test results: {expected}")
for i, n in enumerate(numbers):
    print(f"{i+1}. { {n, intersperse(numbers, delimiters)[0]})
```