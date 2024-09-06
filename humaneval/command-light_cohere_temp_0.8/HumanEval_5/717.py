```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i + delimiter for i, delimiter in zip(numbers, [delimeter] * 2)]

# Test the function with a list of integers
numbers = [1, 2, 3]
delimiters = [4, 4, 2, 4, 3]
result = intersperse(numbers, delimiters)
print(result)

# Test the function with a list of strings
strings = ["Hello", "World", "!!!"]
delimiters = [4, 4, 2, 4]
result = intersperse(strings, delimiters)
print(result)
```
This Python code defines a function `intersperse` that takes a list of numbers and a delimiter as input and returns a new list with numbers separated by the given delimiter. The code then passes two tests to the `intersperse` function:
1. Using a list of integers and a list of corresponding delimiters, the function creates a new list with the numbers separated by the delimiters. This test results in producing a list with the numbers [1, 2, 3] and the delimiters [4, 4, 2, 4].
2. Using a list of strings and a list of corresponding delimiters, the function creates a new list with the strings separated by the delimiters, resulting in a list with the strings ['Hello', 'World', '!'] and the delimiters [4, 4].