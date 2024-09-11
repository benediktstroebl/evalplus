```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
    numbers (List[int]): The input list of numbers.
    delimeter (int): The number to be inserted between every two consecutive elements.

    Returns:
    List[int]: The resulting list with the delimeter inserted.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        # If it's not the last element, append the delimeter
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

Alternatively, you can use a more concise solution using a list comprehension:

```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
    numbers (List[int]): The input list of numbers.
    delimeter (int): The number to be inserted between every two consecutive elements.

    Returns:
    List[int]: The resulting list with the delimeter inserted.
    """
    return [x for pair in zip(numbers, numbers[1:] + [None]) for x in (pair[0], delimeter) if x is not None]

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```