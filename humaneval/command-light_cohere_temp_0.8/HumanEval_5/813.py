```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function with simple cases
numbers = [1, 2, 3]
print("Test 1: ", end="")
print(*inperse(numbers, 2))  # Output: [3, 5, 7, 9]

numbers = [1, 2, 3, 4, 5]
print("Test 2: ", end="")
print(*inperse(numbers, 3))  # Output: [2, 4, 6, 10]

numbers = [1, 2, 3, 4, 5, 6]
print("Test 3: ", end="")
print(*inperse(numbers, 4))  # Output: [3, 8, 12, 16]

numbers = [1, 2, 3, 4, 5, 6, 7]
print("Test 4: ", end="")
print(*inperse(numbers, 3))  # Output: [2, 6, 10, 14]

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print("Test 5: ", end="")
print(*inperse(numbers, 2))  # Output: [3, 6, 10, 12]

numbers = [1, 2, 3, 4, 5]
print("Test 6: Error! Incorrect delimiter")  # Should raise an error
```