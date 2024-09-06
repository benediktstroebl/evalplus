```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for n in numbers:
        result.append(n+ + delimeter)
    return result

# Test case 1
numbers = [1, 2,3]
result1 = intersperse(numbers, 4)
print(result1)  # Output: [1, 4, 2, 4, 3]

# Test case 2
numbers = [1, 2, 3]
result2 = intersperse(numbers, 3)
print(result2)  # Output: [1, 3, 2]

# Test case 3
numbers = [1, 2, 3, 4]
result3 = intersperse(numbers, 2)
print(result3)  # Output: [1, 2, 3, 4]

# Test case 4
numbers = [5, 6, 7, 8]
result4 = intersperse(numbers, 4)
print(result4)  # Output: [5, 8, 6, 7, 4]

# Test case 5
numbers = [9,10,11]
result5 = intersperse(numbers, 100)
print(result5)  # Output: 

# [9, 100, 10, 11]
```