```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases 

numbers = [1, 2, 3, 4, 5]
delimiters = [0, 4, 2, 4, 3]  

result = intersperse(numbers, delimiters)
assert list(result) == [1, 4, 2, 4, 3, 5]

numbers = [1, 2, 3, 4, 5]
result = intersperse(numbers, 100)
assert list(result) == [1, 102, 3, 104, 5]

# Correct? The above will fail if the delimiter is not a positive integer. 
```