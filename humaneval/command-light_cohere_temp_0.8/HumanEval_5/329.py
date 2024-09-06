```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+delimiter for i,j in zip(numbers,numbers[1:]+[delimeter])] + numbers[0:]

# Unit tests
numbers = [1,2,3]
delimiters = [0, 4]
expected = [1, 4, 2, 4, 3]
print(f"Result: {expected}")
```