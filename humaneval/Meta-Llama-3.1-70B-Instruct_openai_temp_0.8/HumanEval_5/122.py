```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list 'numbers'

    Args:
        numbers (List[int]): A list of integers
        delimiter (int): The number to be inserted between every two consecutive elements

    Returns:
        List[int]: The modified list with the delimiter inserted
    """
    result = []
    for i, num in enumerate(numbers):
        if i > 0:
            result.append(delimiter)
        result.append(num)
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and a delimiter as input, and returns a new list with the delimiter inserted between every two consecutive elements. The function uses a for loop to iterate over the input list, and appends the delimiter before each element except the first one. The result is then returned. The script includes test cases to verify the correctness of the function.