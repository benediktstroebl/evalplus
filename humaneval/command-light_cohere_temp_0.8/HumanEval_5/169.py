```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases
numbers = [1, 2, 3]
delimiters = [4, 8]

result = intersperse(numbers, delimiters)
print(result)  # Expected output: [1, 4, 8, 2, 12, 3, 16, 4, 20, 8, 23]

numbers = [1, 2, 3, 4, 5]
delimiters = [4, 8]

result = intersperse(numbers, delimiters)
print(result)  # Expected output: [1, 4, 8, 12, 16, 20, 23]
``` 
This code defines the `intersperse` function that takes a list of numbers and a delimiter as input and returns a list with the numbers separated by that delimiter. The test cases demonstrate the example usage of this function.