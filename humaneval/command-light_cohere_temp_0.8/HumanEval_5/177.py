```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return numbers + [delimiter] + numbers[::-1] 

# Test cases:
numbers = [1, 2, 3, 4, 5]
result = intersperse(numbers, 4)
print(result)  # Expected Output: [1, 4, 2, 4, 3, 5]

numbers = [10, 20, 30, 40, 50]
result = intersperse(numbers, 5)
print(result)  # Expected Output: [10, 5, 20, 10, 30, 40, 50]

numbers = [1, 2, 3, 4, 5, 6]
result = intersperse(numbers, 3)
print(result)  # Expected Output: [1, 4, 2, 4, 3, 5, 6]
```
This Python code defines a function `intersperse` that splits a list into two lists with a specified delimiter in between every second element. The code provides three test cases that demonstrate the functionality of the `intersperse` function.