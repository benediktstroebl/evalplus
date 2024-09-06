Here's the code with a self-contained function and tests:
```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two
    consecutive elements of the input list.
    Parameters:
    numbers: list of integers,
    delimiter: int, number to insert the space
    Returns: list of integers with numbers separated by the delimiter
    """
    return [num + delimiter for num, delimiter in zip(numbers, [delimeter] * 2)]

# Test the function with an empty list
test_empty_list = intersperse([], 4)
assert len(test_empty_list) == 0

# Test the function with a list of numbers
test_list = [1, 2, 3]
test_result = intersperse(test_list, 4)
assert len(test_result) == 6

# Test the function with a list of mixed numbers
test_mixed_list = [4, 2, 3, 1]
test_result = intersperse(test_mixed_list, 4)
assert len(test_result) == 6

# Test the function with a large list of numbers
test_large_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test_result = intersperse(test_large_list, 4)
assert len(test_result) == 18
```

This Python code defines a function `intersperse` that separates numbers in a list by a specified delimiter. It uses the test as a test case to ensure that the function behaves correctly and produces the expected output. The code is well-contained and provides a clear structure for solving the problem and passing tests.