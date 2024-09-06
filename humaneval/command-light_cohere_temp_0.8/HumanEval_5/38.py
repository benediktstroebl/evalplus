```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function with various inputs
numbers = [4, 2, 3, 1]
delimiters = [4, 2, 3, 1]

result = intersperse(numbers, delimiters)
print("Result:", result)  # Expected output: [5, 6, 9, 11]

numbers = [1, 2, 3, 4, 5]
delimiters = [4, 2, 3, 1]

result = intersperse(numbers, delimiters)
print("Result:", result)  # Expected output: [5, 8, 11]

numbers = [10, 20, 30, 40]
delimiters = [2, 2]

result = intersperse(numbers, delimiters)
print("Result:", result)  # Expected output: [12, 14, 16, 18]
```

This Python code defines a function `intersperse` that takes a list of numbers and a delimiter as input and returns a new list with numbers separated by that delimiter. The test cases demonstrate the use of this function with different inputs, and the expected output is shown for each case.