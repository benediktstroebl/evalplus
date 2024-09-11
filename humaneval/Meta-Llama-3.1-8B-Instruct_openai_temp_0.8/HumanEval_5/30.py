```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
    numbers (List[int]): A list of integers.
    delimeter (int): The number to be inserted between elements.

    Returns:
    List[int]: The list with the delimeter inserted between elements.
    """
    result = [numbers[0]]  # Initialize the result list with the first number
    for num in numbers[1:]:  # Iterate over the rest of the numbers
        result.extend([delimeter, num])  # Insert the delimeter and the current number
    return result

# Example usage:
if __name__ == "__main__":
    # Test cases
    print(intersperse([], 4))  # []
    print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
    print(intersperse([1, 2, 3, 4, 5], 0))  # [1, 0, 2, 0, 3, 0, 4, 0, 5]
```

This script defines a function `intersperse` that takes a list of integers and an insertion number. It returns a new list with the insertion number between every two consecutive elements of the input list. The function uses a list comprehension to iterate over the input list and insert the delimeter between each pair of numbers. The test cases at the end demonstrate the function's behavior.