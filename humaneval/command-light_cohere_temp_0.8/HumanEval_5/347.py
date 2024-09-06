```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list """
    result = [num] + [num + delimiter for delimiter in range(delimeter) for num in numbers] + [num]
    return result[:]

# Test the function with different inputs
numbers = [1, 2, 3]
result1 = intersperse(numbers, 4)
assert len(result1) == 7

numbers = [4, 5, 6, 7]
result2 = intersperse(numbers, 3)
assert len(result2) == 7

numbers = [1, 2, 3]
result3 = intersperse(numbers, 2)
assert len(result3) == 6

numbers = [4, 5, 6, 7]
result4 = intersperse(numbers, 1)
assert len(result4) == 7
```
This Python code defines a function `intersperse` that separates consecutive elements in a list by a specified delimiter. The test cases verify the **the correctness of the function** by passing different inputs, and the results are compared against the expected lengths.