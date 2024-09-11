```python
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers`

    Args:
        numbers (List[int]): Input list of integers
        delimiter (int): Number to be inserted between consecutive elements

    Returns:
        List[int]: List of integers with delimiter inserted
    """
    if not numbers:  # Check if input list is empty
        return []

    result = [numbers[0]]  # Initialize result list with first element from input list
    for num in numbers[1:]:  # Iterate over the rest of the list
        result.append(delimiter)  # Add delimiter to result list
        result.append(num)  # Add current number to result list
    return result


# Test cases
if __name__ == "__main__":
    print(intersperse([], 4))  # Output: []
    print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and a delimiter integer, and returns a new list with the delimiter inserted between every two consecutive elements. It then includes a test case in the `if __name__ == "__main__":` block to verify that the function behaves as expected.