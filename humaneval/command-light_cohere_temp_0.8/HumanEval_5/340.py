```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list
    :param numbers: list of integers
    :param delimiter: integer
    :return: list of integers with the delimiter inserted
    """
    return [num != delimiter and delimiter + 1 or num for num in numbers]

# Test cases
numbers = [1, 2, 3]
print(inperse(numbers, 4))  # Output: [1, 4, 2, 4, 3]

numbers = [1, 2, 3, 4, 5]
print(inperse(numbers, 4))  # Output: [1, 4, 2, 4, 5]

numbers = [10, 11, 12]
print(inperse(numbers, 13))  # Output: [10, 13, 11, 12]

numbers = [10, 11, 12, 13]
print(inperse(numbers, 13))  # Output: [10, 13, 11, 12]
```
This script defines a function `inperse` that performs the task of inserting a number `delimiter` between every two consecutive elements of an input list.  The result by iterating through the list and checking if the current element is the delimiter or not, then adding the delimiter and incrementing it.