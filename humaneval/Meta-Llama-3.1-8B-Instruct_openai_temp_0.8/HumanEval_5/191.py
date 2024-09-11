```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`

    Args:
        numbers (List[int]): The input list of integers
        delimeter (int): The number to be inserted between elements

    Returns:
        List[int]: The list with the delimeter inserted between elements

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:
        return numbers  # Return empty list if input list is empty

    result = [numbers[0]]  # Start with the first element of the input list
    for num in numbers[1:]:  # Iterate over the rest of the list
        result.append(delimeter)  # Insert the delimeter before each element
        result.append(num)
    return result


# Test the function
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This script uses a simple loop to iterate over the input list, inserting the delimeter before each element (except the first one). The result is a new list with the delimeter inserted between elements.