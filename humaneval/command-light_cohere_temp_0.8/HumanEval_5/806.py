Here's the Python script with the function `intersperse` that inserts a number `delimiter` between every two consecutive elements of the input list:
```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter if i < len(numbers) - 1 else num for i, num in enumerate(numbers)]
# Test the function
numbers = [1, 2, 3, 4]
result = intersperse(numbers, 4)
print(result)  # expected output: [1, 4, 2, 4, 3]
```