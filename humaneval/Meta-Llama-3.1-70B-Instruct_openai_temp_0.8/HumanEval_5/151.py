```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
    numbers (List[int]): The input list of numbers.
    delimiter (int): The number to be inserted between every two consecutive elements.

    Returns:
    List[int]: The resulting list with the delimiter inserted.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:  # Check if it's not the last element
            result.append(delimiter)
    return result

# Example usage:
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

Alternatively, you can use a more concise approach using list comprehension and the `itertools.chain` function:

```python
from typing import List
import itertools

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
    numbers (List[int]): The input list of numbers.
    delimiter (int): The number to be inserted between every two consecutive elements.

    Returns:
    List[int]: The resulting list with the delimiter inserted.
    """
    return list(itertools.chain(*[[num, delimiter] if i < len(numbers) - 1 else [num] for i, num in enumerate(numbers)]))

# Example usage:
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```