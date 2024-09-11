```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): The input list of integers
        delimeter (int): The number to be inserted between consecutive elements

    Returns:
        List[int]: The modified list with the delimeter inserted
    """
    if not numbers:  # Check if the list is empty
        return numbers
    
    result = [numbers[0]]  # Initialize the result list with the first element of numbers
    for i in range(1, len(numbers)):  # Iterate over the rest of the elements in numbers
        result.extend([delimeter, numbers[i]])  # Append the delimeter and the current element to the result list
    return result


# Test cases
print(intersperse([], 4))
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```