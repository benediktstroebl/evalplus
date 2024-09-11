```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`

    Args:
        numbers (List[int]): The input list of integers
        delimeter (int): The number to be inserted between every two consecutive elements

    Returns:
        List[int]: The modified list with the delimeter inserted
    """
    if not numbers:
        # If the input list is empty, return it as is
        return numbers
    
    result = [numbers[0]]
    for num in numbers[1:]:
        # Append the delimeter to the result list, then append the current number
        result.extend([delimeter, num])
    
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers `numbers` and a delimeter `delimeter` as input, and returns a new list where the delimeter is inserted between every two consecutive elements of the input list. The function uses a simple iterative approach to build the resulting list. The test cases at the end of the script demonstrate the function's behavior for both an empty input list and a non-empty input list.