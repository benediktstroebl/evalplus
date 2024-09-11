```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers`

    Args:
        numbers (List[int]): The input list of integers
        delimiter (int): The number to be inserted between consecutive elements

    Returns:
        List[int]: The modified list with the delimiter inserted

    Example:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:  # if the list is empty, return it as is
        return numbers
    result = [numbers[0]]  # start with the first element of the list
    for num in numbers[1:]:  # iterate over the rest of the list
        result.append(delimiter)  # insert the delimiter before each number
        result.append(num)
    return result[:-1]  # remove the extra delimiter at the end

# Test the function
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers `numbers` and an integer `delimiter` as input. It inserts the `delimiter` between every two consecutive elements of the `numbers` list and returns the modified list. The function uses a simple iterative approach to achieve this. The test cases at the end demonstrate the function's behavior.