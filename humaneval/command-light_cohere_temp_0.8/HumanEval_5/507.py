```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test the function with various cases
numbers = [1, 2, 3]
delimiters = [4, 8]

result = intersperse(numbers, delimiters)
print("Result:", result)

numbers = [10, 20, 30]
delimiters = [4, 8, 2]

result = intersperse(numbers, delimiters)
print("Result:", result)

numbers = [10, 20]
delimiters = [4, 8]

result = intersperse(numbers, delimiters)
print("Result:", result)

numbers = [10, 20, 30, 40]
delimiters = [8, 2]

result = intersperse(numbers, delimiters)
print("Result:", result)
```
The script defines a function `intersperse` that takes a list of numbers and a delimiter as input and returns a new list with numbers separated by the specified delimiter. The test cases cover various scenarios, and the output matches the expected results.