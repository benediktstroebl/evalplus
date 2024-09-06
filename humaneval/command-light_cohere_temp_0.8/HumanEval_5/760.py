```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list.
    :param numbers: list of integers
    :param delimiter: int
    :return: list of integers with separators
    """
    new_list = [num for num in numbers] + [delimiter]
    new_list += [num for num in numbers[1:]] + [delimiter]
    return new_list

# Test case 1
input_numbers = [1, 2, 3]
result = intersperse(input_numbers, 4)
assert list(result) == [1, 4, 2, 4, 3]

# Test case 2
input_numbers = [1, 2, 3]
result = intersperse(input_numbers, 1000)
assert list(result) == [1 1000, 2 1000, 3 1000]

# Test case 3
input_numbers = [1, 2, 3, 4, 5]
result = intersperse(input_numbers, 100)
assert list(result) == [1 100, 2 100, 3 100, 4 100, 5 100]
```