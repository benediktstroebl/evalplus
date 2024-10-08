```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): The input list of numbers.
        delimiter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The modified list with the delimiter inserted.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

Alternatively, you can use a list comprehension and the `itertools.chain` function to achieve the same result in a more concise way:

```python
from typing import List
import itertools

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): The input list of numbers.
        delimiter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The modified list with the delimiter inserted.
    """
    return list(itertools.chain(*[(num, delimiter) for num in numbers[:-1]], [numbers[-1]])) if numbers else []

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

However, the first implementation is generally more readable and maintainable, especially for those who are not familiar with the `itertools` module.