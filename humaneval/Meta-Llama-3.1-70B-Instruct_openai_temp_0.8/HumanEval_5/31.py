```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The list of numbers to intersperse.
        delimiter (int): The number to insert between every two consecutive elements.

    Returns:
        List[int]: The interspersed list of numbers.
    """
    # Initialize an empty list to store the interspersed numbers
    interspersed_numbers = []

    # Iterate over the input list of numbers with their indices
    for i, num in enumerate(numbers):
        # Append the current number to the interspersed list
        interspersed_numbers.append(num)

        # If the current number is not the last number in the list, append the delimiter
        if i < len(numbers) - 1:
            interspersed_numbers.append(delimiter)

    # Return the interspersed list of numbers
    return interspersed_numbers


# Test cases
print(intersperse([], 4))  # Expected output: []
print(intersperse([1, 2, 3], 4))  # Expected output: [1, 4, 2, 4, 3]
```

This script defines the `intersperse` function as specified and includes test cases to demonstrate its usage. You can run this script directly in a Python interpreter or save it to a file and run it as a standalone Python program.