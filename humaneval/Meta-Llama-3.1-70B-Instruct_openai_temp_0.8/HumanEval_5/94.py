```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Inserts a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of numbers.
        delimeter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The resulting list with delimeter inserted.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        # If it's not the last number, append the delimeter
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result

# Test cases
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```

Alternatively, you can also use the `itertools` module to achieve the same result with a more concise code:

```python
import itertools
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Inserts a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of numbers.
        delimeter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The resulting list with delimeter inserted.
    """
    return [x for pair in itertools.zip_longest(numbers, numbers[1:], fillvalue=delimeter) for x in pair]

# Test cases
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```