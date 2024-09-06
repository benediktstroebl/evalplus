```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of the input list.

    : exempted cases:
        - empty list -> []
        - list with one element -> [that element]
        - list with repeated elements -> list of that repeated element(s)
        - otherwise -> list of integers
    """ 
    return List([i, delimeter] + [i + j for i, j in zip(numbers, numbers[1:]) + [delimeter] * (len(numbers) - 2))
# Generate sample input/output pairs for docstrings
numbers = [1, 2, 3, 4, 5]
delimiter = 4
result = intersperse(numbers, delimiter)
print(f"Input: {result}")  # Output: [1, 4, 2, 4, 3, 5]
print(f"Expected Output: [{1, 4}, {2, 4}, {3, 4}, {4, 5}]")  # Output: Expected Output: [1, 4, 2, 4, 3, 5]
```