```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list `numbers'.
    
    Args:
        numbers (List[int]): A list of integers.
        delimiter (int): The number to be inserted between every two consecutive elements.
    
    Returns:
        List[int]: The list with the delimiter inserted between every two consecutive elements.
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

This script defines a function `intersperse` that takes a list of numbers and a delimiter as input. It initializes an empty list `result` to store the output. Then, it iterates over the input list, appending each number to `result` and appending the delimiter after each number except the last one. Finally, it returns the resulting list.

You can run this script to test the `intersperse` function with different inputs. The test cases at the end of the script demonstrate its usage and expected output.