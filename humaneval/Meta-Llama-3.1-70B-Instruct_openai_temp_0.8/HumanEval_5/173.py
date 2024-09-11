```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'
    
    Args:
        numbers (List[int]): A list of integers.
        delimiter (int): A number to be inserted between every two consecutive elements.

    Returns:
        List[int]: A new list with the delimiter inserted between every two consecutive elements.
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

This script uses a for loop with the enumerate function to iterate over both the index and values of the input list. It appends each number to the result list, and if it's not the last number in the list, it also appends the delimiter. The function then returns the resulting list. The test cases at the end demonstrate the function's behavior with the examples provided.