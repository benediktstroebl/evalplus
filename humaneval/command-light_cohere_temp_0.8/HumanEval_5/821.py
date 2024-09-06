```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function
numbers = [1, 2, 3]
delimiters = [4, 8]
result = intersperse(numbers, delimiters)

print("Result:", result)

# Test with empty list
numbers = []
result = intersperse(numbers, delimiters)

print("Result:", result)
``` 
This script defines a function `intersperse` that takes a list of integers and a delimiter as input, and returns a new list with the numbers separated by that delimiter. The function uses the method `enumerloop` with `i` and `num` as the iteration variables to add the `delimiter` to the number every two consecutive elements in the input list.