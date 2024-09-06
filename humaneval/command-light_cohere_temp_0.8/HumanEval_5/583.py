```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+delimeter for i,j in zip(numbers,numbers[1:])] + numbers[-1:]

# Test cases
numbers = [1, 2, 3, 4]
print(intersperse(numbers, 4))  # expected output: [1, 4, 2, 4, 3]

numbers = [1, 2, 3, 4, 5]
print(intersperse(numbers, 3))  # expected output: [1, 4, 5, 8]

numbers = [10, 11, 12, 13]
print(intersperse(numbers, 4))  # expected output: [10, 7, 11, 13]

numbers = [1, 2, 3, 4, 5, 6, 7]
print(intersperse(numbers, 5))  # expected output: [1, 6, 7, 8, 10]
```