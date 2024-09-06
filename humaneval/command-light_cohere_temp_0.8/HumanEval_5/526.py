```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num in numbers] + [num + delimeter*2 for num in numbers]

# Test case 1
numbers = [1, 2, 3]
delimiters = [4, 4, 8]
expected = [5, 6, 8]
print(f"Test case 1: {expected}, {numbers}")

# Test case 2
numbers = [1, 2, 3]
delimiters = [4]
expected = [5, 7]
print(f"Test case 2: {expected}, {numbers}")

# Test case 3
numbers = [1, 2, 3, 4, 5]
delimiters = [4, 8]
expected = [9, 13]
print(f"Test case 3: {expected}, {numbers}")
```
This Python script defines a function `intersperse` that takes a list of integers and a delimiter as input and returns a new list with numbers separated by that delimiter. It uses a basic iteration to achieve this, adding the delimiter to the previous number, and then adding twice the delimiter to the current number. The script also provides three test cases to verify the functionality of the `intersperse` function.