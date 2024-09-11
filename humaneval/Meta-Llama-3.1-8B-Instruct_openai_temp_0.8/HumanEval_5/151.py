```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`

    Args:
        numbers (List[int]): The input list of integers
        delimeter (int): The number to be inserted between elements of the list

    Returns:
        List[int]: The list with the delimeter inserted between elements

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:  # If the list is empty, return it as is
        return numbers

    result = [numbers[0]]  # Start with the first element of the list
    for num in numbers[1:]:  # Iterate over the rest of the list
        result.append(delimeter)  # Add the delimeter to the result
        result.append(num)  # Add the current number to the result
    return result

# Test the function
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and a number to be inserted between elements. It iterates over the list, adding the delimeter and each number to the result list. If the input list is empty, it returns the list as is. The function is then tested with two examples.