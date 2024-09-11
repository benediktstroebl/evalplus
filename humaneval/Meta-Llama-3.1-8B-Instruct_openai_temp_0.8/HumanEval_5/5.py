```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of numbers.
        delimeter (int): The number to insert between elements.

    Returns:
        List[int]: The modified list with the delimeter inserted.

    Example:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    result = [numbers[0]]
    for num in numbers[1:]:
        result.extend([delimeter, num])
    return result[:-1] if result and result[-1] == delimeter else result

# Test cases
print(intersperse([], 4))
print(intersperse([1, 2, 3], 4))
```

In this code, we iterate over the input list `numbers` starting from the second element (at index 1). For each element, we append the delimeter and then the element itself to the result list. This effectively inserts the delimeter between every two consecutive elements. The last element is not followed by a delimeter if the list ends with an odd number of elements, to avoid unnecessary delimiters.