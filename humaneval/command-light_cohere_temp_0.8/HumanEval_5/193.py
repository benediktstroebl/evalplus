```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimiter' between every two consecutive elements of input list"""
    return [x+y+delimiter for x, y in zip(numbers, numbers[1:])] + [numbers[-1]]

# Test cases
test_numbers = [1,2,3]
test_delimiter = 4
test_result = intersperse(test_numbers, test_delimiter)
print("Test case 1:", end:)
print(test_result)

test_numbers = [4,3,2,1]
test_delimiter = 3
test_result = intersperse(test_numbers, test_delimiter)
print("Test case 2:", end)>", print(test_result)

test_numbers = [1,2,3,4]
test_delimiter = [0,1]
test_result = intersperse(test_numbers, test_delimiter)
print("Test case 3:", end)>", print(test_result)

test_numbers = [4,3,2,1]
test_delimiter = [4]+[0]
test_result = intersperse(test_numbers, test_delimiter)
print("Test case 4:", end)>", print(test_result)
```

This code defines a Python function `intersperse` that takes two parameters: a list of integers `numbers` and an integer `delimiter`. It then creates a new list by inserting the `delimiter` between every two consecutive elements of the input list. The output of the test cases demonstrate how the function behaves for different scenarios.