```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): The input list of integers.
        delimiter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The modified list with the delimiter inserted between every two consecutive elements.
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

In this script, we iterate over the input list `numbers` using `enumerate` to get both the index and the value of each element. We append each element to the result list, and if it's not the last element, we also append the delimiter. The function then returns the modified list.