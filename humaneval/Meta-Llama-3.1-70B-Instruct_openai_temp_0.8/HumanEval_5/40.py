```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): The input list of integers.
        delimiter (int): The number to be inserted between consecutive elements.

    Returns:
        List[int]: The modified list with the delimiter inserted.
    """
    result = []  # Initialize an empty list to store the result
    for i, num in enumerate(numbers):  # Iterate through the input list with index and value
        result.append(num)  # Append the current number to the result list
        if i < len(numbers) - 1:  # Check if it's not the last element in the list
            result.append(delimiter)  # Append the delimiter if it's not the last element
    return result  # Return the modified list


# Example use cases
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and a delimiter as input, and returns a new list with the delimiter inserted between every two consecutive elements of the input list. The function uses a for loop to iterate through the input list, appending each number and the delimiter (if it's not the last element) to a result list. The script also includes example use cases to demonstrate the function's behavior.