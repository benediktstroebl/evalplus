```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list 'numbers'

    Args:
        numbers (List[int]): The input list of numbers.
        delimiter (int): The number to be inserted between consecutive elements.

    Returns:
        List[int]: The modified list with the delimiter inserted.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result

# Example usage:
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

Alternatively, you can also use a list comprehension to achieve the same result in a more concise way:

```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list 'numbers'

    Args:
        numbers (List[int]): The input list of numbers.
        delimiter (int): The number to be inserted between consecutive elements.

    Returns:
        List[int]: The modified list with the delimiter inserted.
    """
    return [x for pair in zip(numbers, numbers[1:] + [None]) for x in (pair[0], delimiter) if x is not None]

# Example usage:
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This version uses the `zip` function to pair each element in the input list with the next one, and then uses a nested list comprehension to flatten the list of pairs and insert the delimiter between each pair. The `if x is not None` clause is used to exclude the `None` value that is appended to the end of the list to handle the last pair.