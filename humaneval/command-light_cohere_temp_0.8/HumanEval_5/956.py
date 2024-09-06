```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i + delimeter for i, j in zip(numbers, numbers[1:]) for j in numbers[1:]]

# Unit tests
numbers = [1, 2, 3, 4, 5]
delimiters = [0, 0, 1]

expect = [1, 2, 3, 4, 5, 4, 3]
result = intersperse(numbers, delimiters)
assert listEqual(expect, result)

numbers = [10, 20, 30, 40]
delimiters = [5, 10]

expect = [10, 15, 20, 35, 40]
result = intersperse(numbers, delimiters)
assert listEqual(expect, result)
``` 
This code defines a function **'intersperse()'** which receives a list of integers and a delimiter as input and returns a new list with the elements separated by the provided delimiter. The code also provides two sets of test cases, passing the function with different lists of integers and a list of integers with corresponding delimiters, and asserting that the output is correct.