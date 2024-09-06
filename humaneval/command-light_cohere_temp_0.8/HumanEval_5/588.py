```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list.
    Numbers are separated by at least least, the delimiter is inserted.
    Args:
        numbers: List[int], input list of numbers
        delimiter: int, the number to separate consecutive elements
    Returns:
        List[int], list of numbers with a delimiter inserted
    """
    return [x + delimeter for x, y in zip(numbers, numbers[1:])] + numbers

# Test case 1
print(inperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]

# Test case 2
print(inperse([1, 2, 3], 2))  # [1, 2, 3, 2, 3]

# Test case 3
print(inperse([1, 2, 3, 4, 5], 3))  # [1, 2, 3, 4, 5]

# Test case 4
print(inperse([1, 2, 3], 0))  # [1, 2, 3]
```
This Python script defines a function `inperse` that separates a list of numbers with a specified delimiter. The function uses a array `zip` to insert the delimiter between every two consecutive elements of the list. The test cases show the essential function behavior.