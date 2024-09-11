### Interspersing Numbers in a List
```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
    numbers (List[int]): Input list of integers
    delimeter (int): Number to be inserted between elements

    Returns:
    List[int]: List with delimeter inserted between every two consecutive elements

    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if i < len(numbers) - 1:  # Check if not last element
            result.append(delimeter)
    return result

# Example usage:
numbers = [1, 2, 3]
delimeter = 4
print(intersperse(numbers, delimeter))  # Output: [1, 4, 2, 4, 3]
```
This script defines a function `intersperse` that takes a list of integers and a delimeter integer as input. It iterates over the input list, appending each element to the result list, and then appends the delimeter if it's not the last element in the list. The function returns the resulting list with the delimeter inserted between every two consecutive elements.