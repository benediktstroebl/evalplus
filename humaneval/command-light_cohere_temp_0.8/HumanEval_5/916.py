```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = [num] + [num] + [delimeter] * (len(numbers) - 2) + [num] + [delimiter] * (len(numbers) - 2)
    return result
numbers = [1, 2, 3]
print(intersperse(numbers, 4))  # Expected output: [1, 4, 2, 4, 3]
```
This Python code defines a function `intersperse` that takes a list of numbers and a delimiter as input and returns a new list with the numbers interspersed with the delimiter. The code also provides a test case to verify the correctness of the `intersperse` function.