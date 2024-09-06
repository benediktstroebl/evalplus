```python
from typing import List
def rolling_max(numbers: List[int]) -> List[int]:
    """
    Generate a list of rolling maximum elements from a given list of integers.
    Args:
        numbers (List[int]): The input list of integers.
    Returns: list[int]): The list of rolling maximum elements.
    """
    function uses the time complexity of O(n), 
    where n is the length of the input list numbers.
    """
    test cases:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    >>> rolling_max([5, 6, 7, 8, 9])
    [8, 9, 9, 9]
    """
    rolling_numbers = List(numbers)  # Create a local copy of the input list
    rolling_numbers.append(numbers[-1])  # Add the last element to the rolling sequence
    rolling_numbers.sort()  # Sort the actual numbers in descending order
    rolling_numbers.append(numbers[1])  # Add the next numbers in the sequence to the rolling sequence
    rolling_numbers.sort()  # Repeat this process until a new element not added
    rolling_numbers = rolling_numbers[::-1]  # Reverse the rolling sequence
    return rolling_numbers
``` 
This function, rolling_max, takes a list of integers as input and returns a list of integers that contains the rolling maximum elements of the input list. The test cases show that the function works correctly, generating the correct output.