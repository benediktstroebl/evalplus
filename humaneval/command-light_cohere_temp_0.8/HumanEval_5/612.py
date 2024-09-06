```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list
    :param numbers: list of integers 
    :param delimeter: integer 

    :return: list of integers with the delimiter inserted 
    """
    return [num + delimeter if i < len(numbers) - 1 else num for i, num in enumerate(numbers)]

# Test case 1
test_numbers = [1, 2, 3]
test_delimiter = 4
test_result = intersperse(test_numbers, test_delimiter)
print(test_result)  # expected output: [1, 4, 2, 4, 3]

# Test case 2
test_numbers = [1, 2, 3]
test_delimiter = 7
test_result = intersperse(test_numbers, test_delimiter)
print(test_result)  # expected output: [1, 10, 13, 14] 

# Test case 3
test_numbers = [1, 2, 3]
test_delimiter = 0
test_result = intersperse(test_numbers, test_delimiter)
print(test_result)  # expected output: [1, 2, 3] 

# Test case 4
test_numbers = [1, 2, 3]
test_delimiter = 10
test_result = intersperse(test_numbers, test_delimiter)
print(test_result)  # expected output: [11, 12, 13] 
``` 
This script defines a function `intersperse` that adds a specified `delimiter` to the start of every other element in a list. The test cases showcase the expected outputs with different lists and delimiters.