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
    """
    if not numbers:  # If the list is empty, return it as is
        return numbers

    result = [numbers[0]]  # Start with the first element
    for i in range(1, len(numbers)):  # Iterate over the rest of the elements
        result.append(delimiter)  # Insert the delimiter
        result.append(numbers[i])  # Append the current element
    return result

# Example usage:
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script uses a simple loop to iterate over the input list, inserting the delimiter between each pair of consecutive elements. If the input list is empty, it simply returns the empty list.