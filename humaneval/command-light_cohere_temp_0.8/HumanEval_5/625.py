```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+delimiter for i,j in zip(numbers,numbers[1:])] + numbers

# Test cases
numbers = [1, 2, 3, 4, 5]
print(inperseperate(numbers,2))  # expected output: [1, 2, 3, 4, 5, 6]

numbers = [1, 2, 3, 4, 3, 5]
print(inperseperate(numbers,3))  # expected output: [1, 2, 3, 4, 5, 6]

numbers = [10,11,12]
print(inperseperate(numbers,3))  
# expected output: [10, 11, 12, 13, 14, 15]

numbers = [1, 2, 3]
print(inperseperate(numbers,2))  
# expected output: [1, 3, 2]
```