```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list.
    :param numbers: list of integers, delimiter: positive integer
    :return: list of integers with specified delimiter
    """
    return [num + delimiter for delimiter, num in zip(numbers[1:], numbers[::2])]

# Test cases
test_numbers = [4, 2, 3]
test_delimiter = 4
test_result = intersperse(test_numbers, test_delimiter)
print("Test case 1 result:", test_result)

test_numbers = [1, 2, 3]
test_delimiter = 4
test_result = intersperse(test_numbers, test_delimiter)
print("Test case 2 result:", test_result)

test_numbers = [4, 2, 3, 2]
test_delimiter = 4
test_result = intersperse(test_numbers, test_delimiter)
print("Test case 3 result:", test_result)
```

The provided Python script defines a function `intersperse` that inserts a specified `delimiter` between every two consecutive elements in the input list. The test cases demonstrate the result for different scenarios.