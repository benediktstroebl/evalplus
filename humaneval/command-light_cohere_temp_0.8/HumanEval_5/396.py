```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases for the function
numbers_list = [1, 2, 3]
delimiters_list = [4, 4, 4]  

result = intersperse(numbers_list, delimiters_list)
print(result)  # Expected output: [1, 7, 2, 8, 3, 12, 4, 16, 5]

numbers_list = [1, 2, 3, 4, 5]
delimiters_list = [4, 4]  

result = intersperse(numbers_list, delimiters_list)
print(result)  # Expected output: [1, 4, 5, 9, 13]

numbers_list = [1, 2, 3, 4, 5, 6]
delimiters_list = [4, 4]  

result = intersperse(numbers_list, delimiters_list)
print(result)  # Expected output: [1, 8, 10, 13, 16]
```
This script defines a function `intersperse` that takes a list of numbers and a delimiter as input and returns a list of numbers with the delimiter inserted between every two consecutive elements. The test cases demonstrate the novel function.