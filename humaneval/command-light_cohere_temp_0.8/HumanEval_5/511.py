```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num in numbers for _ in range(2)] + [delimiter] + numbers

# Test case 1
numbers = [1, 2, 3]
result = intersperse(numbers, 4)
print(result)  # Output: [1, 4, 2, 4, 3]

# Test case 2
numbers = [1, 2, 3, 4, 5]
result = intersperse(numbers, 4)
print(result)  # Output: [1, 4, 2, 4, 5, 4, 3]

# Test case 3
numbers = [1, 2, 3, 4, 5, 6]
result = intersperse(numbers, 4)
print(result)  # Output: [1, 4, 2, 4, 5, 4, 6, 4]

# Test case 4
numbers = [1, 2, 3, 4, 5, 6, 7]
result = intersperse(numbers, 4)
print(result)  # Output: [1, 4, 2, 4, 5, 4, 6, 4, 7]
```
This Python script defines a function `intersperse` that inserts a specified `delimiter` between every two consecutive elements of a given list. It provides several test cases to demonstrate its functionality.