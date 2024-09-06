```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list
    Returns: list where numbers are interspelled with delimiters
    """
    return [i+delimeter if i != last else i for i,last in zip(numbers,numbers[1:])] + numbers[:-1]

# tests
numbers = [1, 2, 3]
test_numbers = intersperse(numbers, 4)
print(test_numbers)  # expected output: [1, 4, 2, 4, 3]
numbers = [1, 2, 3, 4]
test_numbers = intersperse(numbers, 2)
print(test_numbers)  # expected output: [1, 2, 2, 3, 4]
```