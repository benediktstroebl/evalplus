```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list 'numbers'

    Args:
    numbers (List[int]): A list of integers.
    delimiter (int): The number to be inserted between consecutive elements.

    Returns:
    List[int]: The list with 'delimiter' inserted between consecutive elements.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimiter)
    return result

# Test cases
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```

Alternatively, you can use a list comprehension to achieve the same result in a more concise way:

```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list 'numbers'

    Args:
    numbers (List[int]): A list of integers.
    delimiter (int): The number to be inserted between consecutive elements.

    Returns:
    List[int]: The list with 'delimiter' inserted between consecutive elements.
    """
    return [x for pair in zip(numbers, [delimiter] * len(numbers)) for x in pair][:-1] if numbers else []

# Test cases
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```