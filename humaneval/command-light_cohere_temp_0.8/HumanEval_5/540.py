```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of the input list.
    :param numbers: List[int] - list of integers
    :param delimeter: int - delimiter integer
    :return: List[int] - list of integers with interleaved numbers
    """
    result = [num] + [num + delimeter for num, delimeter in zip(numbers[1:], numbers[::2])] + [num]
    return result

# Unit tests
numbers = [1, 2, 3, 4, 5]
test_interleave = [i, 0] for i in numbers]
test_result = intersperse(numbers, 4)
print(test_result)  # expected: [1, 4, 2, 4, 3, 5]
```