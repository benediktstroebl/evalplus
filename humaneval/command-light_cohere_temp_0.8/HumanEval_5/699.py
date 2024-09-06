```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+delimiter for i,j in zip(numbers, numbers[1:]+[delimeter])] + numbers

# test cases
numbers = [1,2,3,4]
print(intersperse(numbers, 2))  
```