Here's a self-contained Python script with a function that solves the markdown code spacing problem you provided:
```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of the input list.
    Args:
        numbers (List[int]): list of integers
        delimiter (int): Insertion integer
    Returns:
        List[int]: Inserted list with spacing
    """
    result = [num] + [num + delimiter for delimiter in range(delimeter)] + [num]
    return result

# Test case 1: Insert 4 as delimiter
test_case1 = [1, 2, 3]
result1 = intersperse(test_case1, 4)
assert list(result1) == [1, 4, 2, 4, 3]

# Test case 2: Insert 0 as delimiter
test_case2 = [1, 2, 3]
result2 = intersperse(test_case2, 0)
assert list(result2) == [1, 2, 3]
```
This Python script defines a function `intersperse` that inserts a specified delimiter between every two consecutive elements in the input list. The test cases demonstrate the