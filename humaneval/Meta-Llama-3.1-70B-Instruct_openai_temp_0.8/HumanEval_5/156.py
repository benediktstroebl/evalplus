```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
    numbers (List[int]): A list of integers.
    delimiter (int): A number to be inserted between every two consecutive elements.

    Returns:
    List[int]: A new list with the delimiter inserted.
    """
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the input list
    for i, num in enumerate(numbers):
        # Add the current number to the result
        result.append(num)
        
        # If it's not the last number in the list, add the delimiter
        if i < len(numbers) - 1:
            result.append(delimiter)
    
    # Return the result
    return result


# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

Alternatively, you can use a more Pythonic way to achieve this using list comprehension and the `itertools.chain` function:

```python
from typing import List
import itertools

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
    numbers (List[int]): A list of integers.
    delimiter (int): A number to be inserted between every two consecutive elements.

    Returns:
    List[int]: A new list with the delimiter inserted.
    """
    # Use list comprehension to insert the delimiter between every two numbers
    # and chain the resulting lists together
    return list(itertools.chain(*[[num, delimiter] if i < len(numbers) - 1 else [num] for i, num in enumerate(numbers)]))


# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```