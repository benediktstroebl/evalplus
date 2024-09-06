```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers + [delimiter] 

# Test case 1: Basic function usage
numbers = [1, 2, 3]
result = intersperse(numbers, 4)
print(result)  # Expected Output: [1, 4, 2, 4, 3]

# Test case 2: Lists with different lengths
numbers = [1, 2, 3, 4, 5]
result = intersperse(numbers, 4)
print(result)  # Expected Output: [1, 4, 2, 4, 3, 5]

# Test case 3: Empty list
numbers = []
result = intersperse(numbers, 4)
print(result)  # Expected Output: []

# Test case 4: Lists with different delimiters
numbers = [1, 2, 3]
result = intersperse([4, 5], 4)
print(result)  # Expected Output: [4, 5, 1, 5]

# Test case 5: Lists with different elements
numbers = [1, 2, 'three', 4]
result = interspend(numbers, 4)
print(result)  # Expected Output: [1, 4, two, 4, 3]
```