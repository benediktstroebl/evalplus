```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`

    Args:
        numbers (List[int]): The input list of integers
        delimeter (int): The number to be inserted between elements

    Returns:
        List[int]: The modified list with the delimeter inserted
    """
    if not numbers:  # If the list is empty, return it as is
        return numbers

    result = [numbers[0]]  # Start the result with the first element of the input list
    for num in numbers[1:]:  # Iterate over the rest of the list
        result.extend([delimeter, num])  # Insert the delimeter and the current number
    return result


# Test cases
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```