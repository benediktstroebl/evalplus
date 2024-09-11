```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list 'numbers'.
    
    Args:
        numbers: A list of integers.
        delimiter: An integer to be inserted between every two consecutive elements.
    
    Returns:
        A new list with the delimiter inserted between every two consecutive elements.
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:  # Check if it's not the last element
            result.append(delimiter)
    return result


# Test cases
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```

This script defines the `intersperse` function, which iterates over the input list `numbers`. For each number, it appends the number to the result list and then checks if it's not the last element in the list. If it's not the last element, it appends the `delimiter` to the result list. The function returns the resulting list. The script also includes test cases to verify the function's correctness.