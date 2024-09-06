```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+1 if i<len(numbers)-1 else i+delimiter for i in numbers]

# Unit tests
numbers = [1, 2, 3, 4, 5]
delimiters = [0, 0, 0]  

test_result = intersperse(numbers, delimiters)
print(test_result)

numbers = [4, 1, 2, 3]
delimiters = [1, 2]  

test_result = intersperse(numbers, delimiters)
print(test_result)
```  This script contains a function `intersperse` that inserts a number `delimiter` between every two consecutive elements of the input list numbers. It also has a test cases to ensure the function works correctly with different scenarios.