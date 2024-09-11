```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of integers.
        delimeter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The list with the delimeter inserted between every two consecutive elements.

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:  # if the list is empty, return it as is
        return numbers
    
    result = [numbers[0]]  # start with the first element of the list
    for i in range(1, len(numbers)):  # iterate over the rest of the list
        result.append(delimeter)  # insert the delimeter
        result.append(numbers[i])  # insert the current element
    return result

# Test the function
print(intersperse([], 4))
print(intersperse([1, 2, 3], 4))
```

This script defines a function `intersperse` that takes a list of integers `numbers` and an integer `delimeter` as input, and returns a new list with the `delimeter` inserted between every two consecutive elements of `numbers`. The function first handles the edge case where the input list is empty. Then, it iterates over the rest of the list and inserts the `delimeter` and each element in turn. The resulting list is then returned. The script includes docstrings and test cases to demonstrate the function's behavior.