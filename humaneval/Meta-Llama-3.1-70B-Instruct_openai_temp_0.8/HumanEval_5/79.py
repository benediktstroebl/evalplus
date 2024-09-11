```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Inserts a number 'delimiter' between every two consecutive elements of input list 'numbers'.

    Args:
        numbers (List[int]): A list of integers.
        delimiter (int): The number to be inserted between elements.

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
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

In this script, the function `intersperse` takes a list of integers and a delimiter as input, and returns a new list with the delimiter inserted between every two consecutive elements. The function uses a for loop to iterate over the input list, appending each element and the delimiter (if it's not the last element) to the result list. The test cases at the end of the script demonstrate the function's behavior.