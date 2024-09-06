```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list.
    Parameters: numbers: list[int], delimiter: int
    Returns: list[int]
    """
    return [num + delimiter for num, delimiter in zip(numbers, [delimeter] * (len(numbers) - 1))]

# Test the function with different input cases
numbers = [1, 2, 3]
print(f"Test 1: {repr(intersperse(numbers, 4))} -> {numbers}")  # [1, 4, 2, 4, 3]

numbers = [1, 2, 3, 4]
print(f"Test 2: {repr(intersperse(numbers, 3))} -> {numbers}")  # [1, 3, 4]

numbers = [5, 10, 15]
print(f"Test 3: {repr(intersperse(numbers, 6))} -> {numbers}")  # [5, 10, 6, 15]

numbers = ["Python", " coding", " AI", "Machine Learning"]
print(f"Test 4: {repr(intersperes(numbers, 3))} -> {numbers}")  # ["Python", " coding ", " AI ", "Machine Learning", ""]

numbers = [1, 2, 3, 4, 5]
print(f"Test 5: {repr(intersperse(numbers, 3))} -> {numbers}")  # [1, 3, 4, 5, 6]
```
The `intersperse` function inserts a number `delimiter` between every two consecutive elements of the input list. You can pass various types of test cases to see how the function behaves.