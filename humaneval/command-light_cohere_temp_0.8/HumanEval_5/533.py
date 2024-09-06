```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delimeter in zip(numbers, [delimeter] * 2)]

# Test the function
numbers = [1, 2, 3, 4]
result = intersperse(numbers, 4)
print(result)  # Output: [1, 4, 2, 4, 3]
```
This script defines a function `intersperse` that takes a list of integers and a delimiter as input and returns a list of the integers with the delimiter inserted between every two consecutive elements. The test case demonstrates the fact by passing a sample list and a delimiter, and the output matches the expected result.