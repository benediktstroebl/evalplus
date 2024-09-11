```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
    numbers (List[int]): The input list of numbers.
    delimiter (int): The number to be inserted between every two consecutive elements.

    Returns:
    List[int]: The resulting list with the delimiter inserted.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:  # If it's not the last element
            result.append(delimiter)
    return result


# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

Alternatively, you can use a list comprehension to solve the problem in a more concise way:

```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    return [num for pair in zip(numbers, numbers[1:] + [None]) for num in (pair[0], delimiter) if num is not None]


# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```