Here's a Python script that contains a self-contained function that solves the problem of inserting a number `delimiter` between every two consecutive elements of an input list:
```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [i+delimiter for i, next_num in enumerate(numbers, delimiter)]

# Test the function with several cases
numbers = [1, 2, 3, 4, 5]
print(inpersece(numbers, 2))  # expected output: [3, 5, 1, 4, 2, 3]

numbers = [10, 9, 8, 7]
print(inpersece(numbers, 3))  # expected output: [10, 9, 8, 7]

numbers = [1, 2, 3]
print(inpersece(numbers, 4))  # expected output: [1, 4, 2, 4, 3]

numbers = [1, 2, 3, 4, 5]
print(inpersece(numbers, 2))  # expected output: [1, 4, 2, 4, 5]
```
This Python script defines a function `inpersece` that takes a list of integers and an integer `delimiter` as input and returns a new list with the elements separated by the provided `delimiter`. The script then passes this function several test cases and verifies the expected outputs.