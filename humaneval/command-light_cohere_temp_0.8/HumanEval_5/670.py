```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list
    :param numbers: List of integers
    :param delimiter: Integer
    :return: List of integers with separators
    """
    return [num+delimiter for num, delimiter in zip(numbers, delimeter)] + [num for num in numbers if len(zip(numbers, delimeter)) != 2]
# Test
numbers = [1, 2, 3]
delimiters = [0, 4]
result = intersperse(numbers, delimiters)
print(result)
``` 
This Python code defines a function `intersperse` that takes a list of integers and an integer `delimiter` as input and returns a list of integers with the specified delimiter between every two consecutive elements. The code then creates a test cases with a `numbers` list and a `delimiters` list of `0` and `4`. The `result` variable stores the output of the `intersperse` function and is printed to the console.