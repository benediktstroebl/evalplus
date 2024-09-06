```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimiter' between every two consecutive elements of input list"""
    new_list = []
    for i in range(len(numbers) - 1):
        if i != 0:
            new_list.append(numbers[i]) + delimiter + numbers[i+1]
    return new_list[:]

# Test cases
numbers = [4, 12, 8, 3, 9, 7]
result = intersperse(numbers, 7)
print(result)  # Expected output: [4, 12, 8, 9, 7, 12, 8, 3, 9, 7]

numbers = [1, 2, 3, 4, 5, 6]
result = intersperse(numbers, 3)
print(result)  # Expected output: [1, 2, 3, 4, 5, 6, 1, 2, 3]

numbers = [10, 20, 30, 40]
result = intersperse(numbers, 10)
print(result)  # Expected output: [10, 20, 30, 40, 10, 20, 30, 40]
```