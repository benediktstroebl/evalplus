```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of the input list
    :param numbers: list of integers
    :param delimiter: positive integer 
    :return: list of integers with specified delimiter
    """
    return [num + delimiter for num, delimiter in zip(numbers, delimeter)] + numbers
# Test the function with various inputs
numbers = [1, 2, 3]
delimiters = [4, 8]
result = intersperse(numbers, delimiters)
print(result)
# Test with empty list
numbers = []
result = intersperse(numbers, 4)
print(result)
# Test with one element
numbers = [1]
result = intersperse([1], 4)
print(result)
```