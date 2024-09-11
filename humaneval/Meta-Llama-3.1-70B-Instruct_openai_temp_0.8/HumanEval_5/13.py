```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
    numbers (List[int]): A list of integers.
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

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and a delimiter as input. It initializes an empty list `result` to store the output. It then iterates over the input list using `enumerate`, which provides both the index `i` and the value `num` of each element. It appends each number to the `result` list, and if it's not the last element (i.e., `i < len(numbers) - 1`), it also appends the delimiter. Finally, it returns the modified list.