```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.
    
    Args:
    numbers (List[int]): A list of integers.
    delimiter (int): The number to be inserted between every two consecutive elements.
    
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
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines the `intersperse` function as specified. It initializes an empty list `result` to store the output. Then, it iterates over the input list `numbers`, appending each number to `result` followed by the delimiter if it's not the last number in the list. Finally, it returns the `result` list.

The script also includes two test cases to verify the function's behavior.