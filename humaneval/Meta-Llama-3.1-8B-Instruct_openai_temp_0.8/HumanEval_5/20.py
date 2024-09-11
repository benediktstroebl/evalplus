```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): List of integers
        delimeter (int): Number to be inserted as delimiter

    Returns:
        List[int]: List with inserted delimiters

    Example:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result


# Test cases
if __name__ == "__main__":
    print(intersperse([], 4))  # Expected output: []
    print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and a delimiter integer as input, and returns a new list where the delimiter is inserted between every two consecutive elements of the input list. The function uses a simple loop to append each element of the input list to the result, followed by the delimiter, until it reaches the end of the list. The test cases at the end of the script demonstrate the function's behavior with different inputs.