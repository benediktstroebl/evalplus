```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of integers.
        delimiter (int): The number to insert between consecutive elements.

    Returns:
        List[int]: The modified list with the delimiter inserted.

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:  # If the list is empty, return it as is
        return numbers

    result = [numbers[0]]  # Start with the first element
    for num in numbers[1:]:  # Iterate over the rest of the list
        result.append(delimiter)  # Insert the delimiter before each element
        result.append(num)

    return result[:-1]  # Remove the extra delimiter at the end


# Test the function
print(intersperse([], 4))  # Should print []
print(intersperse([1, 2, 3], 4))  # Should print [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that inserts a specified delimiter between each pair of consecutive elements in a given list of integers. If the input list is empty, it returns the list as is. Otherwise, it iterates over the list, inserting the delimiter before each element, and returns the modified list. The test cases at the end demonstrate the function's behavior.