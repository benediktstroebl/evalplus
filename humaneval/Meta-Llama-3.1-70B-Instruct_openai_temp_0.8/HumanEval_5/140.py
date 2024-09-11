```python
from typing import List
from itertools import zip_longest

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'
    
    Args:
        numbers (List[int]): The list of numbers.
        delimiter (int): The delimiter to insert between numbers.
    
    Returns:
        List[int]: The list with the delimiter inserted between every two consecutive elements.
    """
    # Use zip_longest to pair each number with the next one, filling in None for the last number
    pairs = zip_longest(numbers, numbers[1:])
    
    # Use a list comprehension to flatten the pairs and insert the delimiter
    result = [item for pair in pairs for item in (pair[0], delimiter) if item is not None]
    
    # Remove the extra delimiter at the end
    if result and result[-1] == delimiter:
        result.pop()
    
    return result

# Test the function
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

However, a simpler solution would be to just use a for loop:

```python
def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'
    
    Args:
        numbers (List[int]): The list of numbers.
        delimiter (int): The delimiter to insert between numbers.
    
    Returns:
        List[int]: The list with the delimiter inserted between every two consecutive elements.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result

# Test the function
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```