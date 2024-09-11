```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): Input list of integers
        delimeter (int): The number to insert between every two consecutive elements

    Returns:
        List[int]: The modified list with the delimeter inserted
    """
    if not numbers:  # If the input list is empty, return it as is
        return numbers
    result = [numbers[0]]  # Start the result list with the first element of the input list
    for num in numbers[1:]:  # Iterate over the rest of the input list
        result.append(delimeter)  # Insert the delimeter
        result.append(num)  # Append the current number
    return result

# Test cases
print(intersperse([], 4))
print(intersperse([1, 2, 3], 4))
```

This script defines a function `intersperse` that takes a list of integers and a delimeter integer, and returns a new list with the delimeter inserted between every two consecutive elements. It uses a simple iterative approach to build the result list. The function includes docstrings to provide documentation and the test cases are printed at the end to demonstrate the function's behavior.