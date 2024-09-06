```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list.
    Parameters: numbers (List[int]): list of integers
    delimiter (int): integer to be inserted
    Returns: List[int]: list of integers with numbers separated by the 'delimiter'.
    """
    return numbers[:-1] + [delimiter] + numbers[-1:] + [delimiter] + numbers[:-2:]

# Unit tests
numbers = [1, 2, 3, 4, 5]
delimiters = [4, 8]

expected = [1, 4, 8, 2, 3, 5, 8, 4, 5]

print(f'Input: {numbers, delimiters} => Expected Output: {expected})
in resurfacing(numbers, delimiters):
    print()
```