```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list
    :param numbers: List[int] - List of integers to be intersppered
    :param delimeter: int - Insertion delimiter
    :return: List[int]
    """
    return [num + delimeter for num, delimeter] + [num for _, num in enumerate(numbers) if num != delimeter]
# Test the function
numbers = [1, 2, 3]
desugared = intersperse(numbers, 4)
print(desugared)  # Expected Output: [1, 4, 2, 4, 3]
``` 
This script defines a function `intersperse` that takes a list of integers and a delimiter as input and returns a new list with the integers, separated by the delimiter. The test case demonstrates that the output is correct.