```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of numbers.
        delimiter (int): The number to be inserted between every two consecutive elements.

    Returns:
        List[int]: The modified list with delimiter inserted between every two consecutive elements.
    """
    
    # If the input list is empty, return an empty list
    if not numbers:
        return []

    # Initialize the result list with the first element of the input list
    result = [numbers[0]]

    # Iterate over the rest of the elements in the input list
    for num in numbers[1:]:
        # Append the delimiter before each number
        result.extend([delimiter, num])

    return result

# Test the function
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```