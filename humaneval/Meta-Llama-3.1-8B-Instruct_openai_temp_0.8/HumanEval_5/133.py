### Interspersing Numbers in a List
```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list 'numbers'.

    Args:
        numbers (List[int]): Input list of integers.
        delimiter (int): The number to insert between each pair of consecutive elements.

    Returns:
        List[int]: The modified list with the delimiter inserted.

    Examples:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:
        # If the input list is empty, return it as is
        return numbers
    
    result = [numbers[0]]  # Start with the first element
    for i in range(1, len(numbers)):
        # Insert the delimiter before each element except the first one
        result.extend([delimiter, numbers[i]])
    
    # Remove the last occurrence of the delimiter (which was added at the end)
    result.pop()
    
    return result
```
You can test this function using the provided doctests or add your own test cases.