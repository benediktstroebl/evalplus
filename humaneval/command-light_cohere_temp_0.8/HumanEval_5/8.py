```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of the input list.
    Parameters: numbers (list of integers) and delimiter (int).
    Returns: A list of integers with a delimiter inserted between every two
    consecutive elements.
    """
Example:
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    new_list = []
    for i in range(len(numbers)):
        if i % 2 == 0:
            new_list.append(numbers[i])
        new_list.append(delimiter)
    new_list.append(numbers[i+1])
    return new_list

# Test the function with sample input and expected output
test_result = intersperse([1, 2, 3], 4)
print(test_result)  # Output: [1, 4, 2, 4, 3]
``` 
This code defines a function `intersperse` that takes a list of integers and a delimiter as input and returns a new list with the delimiter inserted between every other consecutive element. The test code section provides a function with sample input and expected output.