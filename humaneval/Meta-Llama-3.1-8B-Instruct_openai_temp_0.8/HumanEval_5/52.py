```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`.

    Args:
        numbers (List[int]): The input list of numbers.
        delimeter (int): The number to be inserted between consecutive elements.

    Returns:
        List[int]: The modified list with the delimeter inserted.

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
            result.append(delimeter)
    return result

# Testing the function
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```

In this script, we define a function `intersperse` that takes a list of numbers and an integer as input. We use a for loop with `enumerate` to iterate over the input list and append each number and the delimeter to the result list. We only append the delimeter if it's not the last element in the list to avoid extra delimiters at the end. Finally, we return the modified list and provide some test cases to demonstrate the function's behavior.