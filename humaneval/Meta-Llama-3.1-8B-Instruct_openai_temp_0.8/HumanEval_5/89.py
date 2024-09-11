```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
    numbers (List[int]): The input list of integers.
    delimeter (int): The number to be inserted between the elements.

    Returns:
    List[int]: The modified list with the delimeter inserted.

    Examples:
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    if not numbers:  # If the input list is empty
        return []
    
    result = [numbers[0]]  # Initialize the result list with the first element of input list
    for i in range(1, len(numbers)):  # Iterate over the rest of the input list
        result.append(delimeter)  # Insert the delimeter
        result.append(numbers[i])  # Insert the current element
    return result

print(intersperse([], 4))
print(intersperse([1, 2, 3], 4))
```

This script uses a simple iterative approach to insert the delimeter between every two consecutive elements of the input list. It first checks if the input list is empty, and if so, returns an empty list. Then it initializes the result list with the first element of the input list. It iterates over the rest of the input list, inserting the delimeter and the current element into the result list. Finally, it returns the modified result list.