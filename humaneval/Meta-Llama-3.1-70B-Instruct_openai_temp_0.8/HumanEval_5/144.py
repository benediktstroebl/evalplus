```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list 'numbers'.

    Args:
        numbers (List[int]): A list of integers.
        delimiter (int): The number to be inserted between consecutive elements.

    Returns:
        List[int]: The modified list with the delimiter inserted.
    """

    # Initialize an empty list to store the result
    result = []

    # Iterate over the input list with the index and value
    for i, num in enumerate(numbers):
        # Append the current number to the result list
        result.append(num)
        
        # If it's not the last element, append the delimiter
        if i < len(numbers) - 1:
            result.append(delimiter)

    # Return the modified list
    return result


# Test cases
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```