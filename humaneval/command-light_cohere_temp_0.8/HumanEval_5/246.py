```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delimeter in zip(numbers, [delimeter] * 2)]

# Test cases
numbers = [1, 2, 3]
delimiters = [4, 4, 8]  

result = intersperse(numbers, delimiters)
print("Result:", result)  

numbers = [10, 20, 30]
delimiters = [4]  

result = intersperse(numbers, delimiters)
print("Result:", result) 
``` 
This Python script defines a function `intersperse` that separates consecutive elements in a list by a specified `delimiter`. The function uses a list comprehension to achieve this, and the result is returned as a new list with elements separated by the delimiters.