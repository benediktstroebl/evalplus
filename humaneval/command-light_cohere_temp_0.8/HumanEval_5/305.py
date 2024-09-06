```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]
#Test cases are included within the function

# Test case 1
numbers = [1, 2, 3]
delimiter = 4
expected = [1, 4, 2, 4, 3]
result = intersperse(numbers, delimiter)
assert list(map(int, result)) == expected

# Test case 2
numbers = [1, 2, 3]
delimiter = 4
expected = [1, 4, 2, 4, 3]
result = intersperse(numbers, delimiter)
assert list(map(int, result)) == expected

# Test case 3
numbers = [1, 2, 3, 4, 5]
delimiter = 6
expected = [1, 8, 12, 16, 20]
result = intersperse(numbers, delimiter)
assert list(map(int, result)) == expected

# Test case 4
numbers = [1, 2, 90]
delimiter = 1991
expected = [1, 93, 182]
result = intersperse(numbers, delimiter)
assert list(map(int, result)) == expected
``` 
This Python code defines a function `intersperse` that takes a list of integers and an integer `delimiter` as input, and returns a new list with numbers separated by the specified delimiter. The test cases provided aim to validate the correctness of this function by checking if the resulting list of integers matches the expected output for each case.