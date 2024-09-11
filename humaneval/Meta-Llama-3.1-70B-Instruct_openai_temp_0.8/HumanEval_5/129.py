```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers: A list of integers.
        delimiter: The number to be inserted between consecutive elements.

    Returns:
        A new list with the delimiter inserted between every two consecutive elements.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:  # Don't append delimiter after the last element
            result.append(delimiter)
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([1], 4))  # [1]
```

Alternatively, you can use a more concise solution using a list comprehension:

```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers: A list of integers.
        delimiter: The number to be inserted between consecutive elements.

    Returns:
        A new list with the delimiter inserted between every two consecutive elements.
    """
    return [x for pair in zip(numbers, numbers[1:] + [None]) for x in (pair[0], delimiter) if x is not None]

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([1], 4))  # [1]
```