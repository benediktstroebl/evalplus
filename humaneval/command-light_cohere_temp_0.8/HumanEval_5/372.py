```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + delimeter for num, delim  in zip(numbers, [delimeter]*2)]

# Test cases
numbers = [1, 2, 3]
print(inperseperate(numbers, 4))  # Expected Output: [1, 4, 2, 4, 3]

numbers = [1, 2, 3, 4]
print(inperseperate(numbers, 4))  # Expected Output: [1, 4, 2, 4, 3]

numbers = [10, 11, 12]
print(inperseperate(numbers, 5))  # Expected Output: [10, 5, 11, 12]

# General Test case
numbers = [1, 2, 3, 4, 5]
print(inperseperate(numbers, 6))  # Expected Output: [1, 6, 2, 6, 3, 5]
``` 
This Python script defines a function `inperseperate` that inserts a specified `delimiter` value between every two consecutive elements in a given list. It uses a `zip` to iterate through the list twice, adding the `delimiter` in between each pair of elements.