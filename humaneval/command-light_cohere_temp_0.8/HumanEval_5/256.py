```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of the input list """
    return [x + delimeter if i < len(numbers) - 1 else x for i, x in numbers]

# Tests
numbers = [1, 2, 3]
print(inperseperate(numbers, 2))  # Expected: [1, 2, 3, 2, 3]

numbers = [1, 2, 3, 4, 3]
print(inperseperate(numbers, 2))  # Expected: [1, 3, 4, 3, 2]

numbers = [1, 2, 3]
print(inperseperate(numbers, 4))  # Expected: [1, 2, 3, 4]

```