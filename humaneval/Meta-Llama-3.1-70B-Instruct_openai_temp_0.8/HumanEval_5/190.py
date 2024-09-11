```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
    numbers (List[int]): The input list of integers.
    delimiter (int): The number to be inserted between every two consecutive elements.

    Returns:
    List[int]: A new list with 'delimiter' inserted between every two consecutive elements.

    Examples:
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
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

In the provided code:

1. We define a function `intersperse` with a list of integers `numbers` and an integer `delimiter` as arguments.
2. We initialize an empty list `result` to store the output.
3. We iterate through the input list `numbers` using `enumerate`, which provides both the index `i` and the value `num` of each element.
4. We append each number from the input list to the `result` list.
5. If the current number is not the last element in the list (`i < len(numbers) - 1`), we append the `delimiter` to the `result` list.
6. Finally, we return the `result` list.

The test cases at the end demonstrate the expected output for the given input scenarios.