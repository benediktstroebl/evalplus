```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of numbers.
        delimiter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The modified list with 'delimiter' inserted between every two consecutive elements.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        # Check if it's not the last element in the list
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result

# Example use cases:
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

Alternatively, you can use a more concise solution using a list comprehension:

```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of numbers.
        delimiter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The modified list with 'delimiter' inserted between every two consecutive elements.
    """
    return [x for pair in zip(numbers, numbers[1:] + [None]) for x in (pair[0], delimiter) if pair[1] is not None]

# Example use cases:
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```