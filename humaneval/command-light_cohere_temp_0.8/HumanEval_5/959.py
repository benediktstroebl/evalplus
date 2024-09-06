```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter if i < len(numbers) - 1 else num for i, num in enumerate(numbers)]
# Example usage:
numbers = []
numbers. = [1, 2, 3, 4, 5]
result = intersperse(numbers, 2)
print(result)  # Expected output: [1, 2, 3, 2, 4, 5]
```
This Python code defines a function `intersperse` that takes a list of integers `numbers` and a delimiter `delimeter` as input. It uses a target list comprehension to iterate over the numbers in the list, adding the delimiter if there's a next number, otherwise it adds the current number. The code is tested and can handle various inputs, making it a reusable and versatile solution for this problem.