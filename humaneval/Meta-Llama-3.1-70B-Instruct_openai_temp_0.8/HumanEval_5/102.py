```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list 'numbers'.

    Args:
        numbers (List[int]): A list of integers.
        delimiter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The modified list with the delimiter inserted.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:  # Check if it's not the last element
            result.append(delimiter)
    return result

# Test cases
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and a delimiter as input. It iterates over the input list using `enumerate`, which provides both the index and the value of each element. If the current element is not the last one in the list, it appends the delimiter to the result list after appending the current element. Finally, it returns the modified list.

The test cases at the end demonstrate the function's behavior with an empty list and a list with three elements.