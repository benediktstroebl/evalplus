```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of the input list.
    Args:
        numbers: List of integers, must not be empty, 
         Will raise an error if it is empty.
        delimiter: Integer, number to insert between every two elements
    Returns:
        A list with elements separated by 'delimiter'.
    """
    if not numbers:
        raise ValueError("Input list cannot be empty")
    return [num + delimiter for num, delimiter in zip(numbers, [delimeter for i in range(len(numbers))])]

# Unit tests
numbers = [1, 2, 3]
delimiters = [4, 4, 8]

expected = [1, 4, 8, 2, 8, 3]
result = intersperse(numbers, delimiters)

if result != expected:
    raise AssertionError(f"Expected: {expected}, Got: {result}")
```  This Python code provides a function `intersperse` which takes two arguments: a list of integers and an integer that serves as a delimiter. The function inserts the numbers to the list, separated by the given delimiter. This code also comes with a set of unit tests to ensure the correctness of its functionality.