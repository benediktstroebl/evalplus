```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list.
    :param numbers: list of integers, delimiter: integer
    :return: list of integers with consecutive pairs separated by 'delimiter'
    """
    # test case 1
    numbers = []
    numbers.append(4)
    numbers.append(4)
    return numbers

# test case 2
numbers = [1, 2, 3]
numbers = [1, 2, 3]
numbers = [1, 4, 2, 4, 3]
print(numbers)
print(intersperse(numbers, 4))
```