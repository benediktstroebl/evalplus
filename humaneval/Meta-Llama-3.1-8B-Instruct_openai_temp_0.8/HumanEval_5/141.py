```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`.

    Args:
    numbers (List[int]): The input list of integers.
    delimeter (int): The number to insert between the elements.

    Returns:
    List[int]: A new list with the delimeter inserted between the elements.
    """
    result = []
    for i, num in enumerate(numbers):
        # Append the current number to the result list.
        result.append(num)
        
        # If it's not the last number in the list, append the delimeter.
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result


# Example usage.
if __name__ == "__main__":
    # Test case 1: Empty list.
    print(intersperse([], 4))  # Expected output: []

    # Test case 2: List with 3 elements.
    print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and a delimeter integer as input. It returns a new list where the delimeter is inserted between every two consecutive elements of the input list. The script also includes example usage and test cases as per the provided specification.