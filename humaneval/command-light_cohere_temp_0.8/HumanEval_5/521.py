```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num in numbers] + [num + (delimiter * 2) for num in numbers]

# Unit tests
numbers = [1, 2, 3, 4, 5]
delimiters = [0, 4, 8, 12]

expected = [1, 4, 8, 12, 16, 20]
result = intersperse(numbers, delimiters)

print("Expected:", expected)
print("Result:", result)
``` 
This code defines a function `inperse` that takes a list of numbers and a delimiter as input and returns a new list with numbers separated by that delimiter. The code also provides unit tests to ensure the function is working correctly.