```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases
numbers = [1, 2, 3, 4]
print("Test case 1: ", end="")
print(numbers)
print()

result = intersperse(numbers, 2)
print("Test case 2: ", end="")
print(result)
print()

numbers = [5, 10, 15]
result = intersperse(numbers, 2)
print("Test case 3: ", end="")
print(result)
print()

numbers = [1, 2, 3]
result = intersperse(numbers, 4)
print("Test case 4: ", end="")
print(result)
print()

numbers = [5, 10, 15]
result = intersperse(numbers, 4)
print("Test case 5: ", end="")
print(result)
``` 

This script defines a function `intersperse` that takes a list of integers and a delimiter as input and returns a new list with the numbers interspersed with the specified delimiter. The test cases demonstrate the the use of the `intersperse` function with different sets of numbers and delimiters.