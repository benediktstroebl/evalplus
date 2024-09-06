```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+delimiter for i,j in zip(numbers,numbers[1:]+[delimeter])] + numbers[:-1]

# Unit tests
numbers = [1, 2, 3]
print(inperseperate(numbers, 4))  # [1, 4, 2, 4, 3]
print(inperseperate([10, 20, 30]))  # [10, 20, 30, 10, 20, 30]
```