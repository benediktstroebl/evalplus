Here's a self-contained Python function that solves the markdown code block problem:
```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of the input list.
    :param numbers: list of integers, delimiter: int
    :return: list of integers with spaces inserted
    """
    return [num + delimiter for delimiter, num in zip(numbers[1:], numbers)]


# Test case 1
numbers = [1, 2, 3]
result = intersperse(numbers, 4)
print(result)
# Expected output: [1 4 2 4 3]

# Test case 2
numbers = [1,2,3,4,5]
result = intersperse(numbers, 4)
print(result)
# Expected output: [1 4 5 2 4 5]

# Test case 3
numbers = [1,2,3,4,5,6]
result = intersperse(numbers, 4)
print(result)
# Expected output: [1 4 5 6 1 4 5 6]
```

This script defines a function `intersperse` that inserts a specified `delimiter` after the second element of each consecutive pair in the input list.  The output of this code block is an example of the usage of the `intersperse` function with three different test cases, showcasing the expected output.