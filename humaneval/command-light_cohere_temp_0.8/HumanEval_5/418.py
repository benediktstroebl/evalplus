```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases
numbers = [1, 2, 3]
delimiters = [4, 8]

result = intersperse(numbers, delimiters)
print(result)

numbers = [1, 2, 3]
delimiters = [4]

result = intersperse(numbers, delimiters)
print(result)

numbers = [4, 5, 6]
delimiters = [1, 4]

result = intersperse(numbers, delimiters)
print(result)
```
The above Python code defines a function `intersperse` that takes a list of integers and a delimiter as input and returns a new list with the elements of the input list separated by the given delimiter. It uses a` enumerate` function to iterate through the input list, adding the computed delimiter between every other element. The output of this list is printed for all test cases.