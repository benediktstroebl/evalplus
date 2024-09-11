### Interspersing Numbers in a List
```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`

    Args:
    numbers (List[int]): The input list of integers
    delimeter (int): The number to be inserted between elements

    Returns:
    List[int]: The list with delimeter inserted between elements
    """
    if not numbers:  # if the list is empty, return it as is
        return numbers
    
    result = [numbers[0]]  # start with the first element
    for num in numbers[1:]:  # iterate over the rest of the list
        result.extend([delimeter, num])  # insert delimeter and num into the result list
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([1, 2, 3, 4, 5], 0))  # [1, 0, 2, 0, 3, 0, 4, 0, 5]
```
This script defines a function `intersperse` that takes a list of integers and an insertion number, and returns a new list with the insertion number inserted between each pair of consecutive elements. The test cases demonstrate the function's behavior with empty lists, lists of arbitrary length, and lists with different insertion numbers.