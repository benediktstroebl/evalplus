```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list
    :param numbers: list of integers
    :param delimiter: integer 
    :return: list of integers with delimiter
    """
    new_list = [x]
    for i in range(1, len(numbers)):
        new_list.append(numbers[i-1]) + delimiter + new_list[i]
    return new_list

# Test cases
test_numbers = [1, 2, 3,4,5]
test_delimiter = 4
test_result = intersperse(test_numbers, test_delimiter)
print(test_result)

test_numbers = [4,3,2,1]
test_delimiter = 1
test_result = intersperse(test_numbers, test_delimiter)
print(test_result)

test_numbers = [5,6]
test_delimiter = 4
test_result = intersperse(test_numbers, test_delimiter)
print(test_result)
``` 
The code defines a function `intersperse` that takes in a list of integers and a delimiter as input and then inserts the delimiter between every two consecutive elements. The test cases demonstrate the follow a similar pattern, testing the function with different input scenarios.