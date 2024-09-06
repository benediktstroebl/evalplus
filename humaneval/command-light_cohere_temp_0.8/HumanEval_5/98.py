```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function with various inputs
numbers = [1, 2, 3]
delimiters = [4, 8]

result = intersperse(numbers, delimiters)
print(result)

numbers = [2, 4, 6]
delimiters = [3, 6]

result = intersperse(numbers, delimiters)
print(result)

numbers = [1, 2, 3]
delimiters = [1, 4]

result = intersperse(numbers, delimiters)
print(result)
``` 
This code defines a Python function `intersperse` that takes a list of numbers and a delimiter as input and returns a list of permuted numbers with the specified delimiter. The function uses the why list comprehension to achieve this, where each element in the input list is incremented by the product of the delimiter and the count of the current iteration.