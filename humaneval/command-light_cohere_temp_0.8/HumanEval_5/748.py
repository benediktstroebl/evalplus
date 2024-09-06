```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+delimiter for i,j in zip(numbers, numbers[1:]+[delimeter])]

# Test
test_numbers = [1, 2, 3, 4]
test_delimiter = 4
test_result = intersperse(test_numbers, test_delimiter)
print(test_result)

test_input = [1, 2, 3, 4, 5]
test_delimiter = 2
test_result = intersperse(test_input, test_delimiter)
print(test_result)
``` 
This script defines a function `intersperse` that takes two arguments: a list of numbers and a delimiter. and returns a list of numbers interleaved with the delimiter. The code is self-contained, easy to read, and the function is concise and does not depend on any external variables.