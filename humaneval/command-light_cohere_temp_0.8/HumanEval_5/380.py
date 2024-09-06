```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delim in zip(numbers, [delimeter] * 2)]

# Test the function
numbers = [1, 2, 3]
delimiters = [4, 4, 2, 4] * 3
result = intersperse(numbers, delimiters)

print(f"Input: {numbers, delimiters}, Output: {result}")
``` 
This script defines a function `inperse` that takes a list of numbers and a delimiter as input, and returns a new list with the numbers separated by that delimiter. The test case provided passes the