```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): The input list of numbers
        delimiter (int): The number to be inserted between consecutive elements

    Returns:
        List[int]: The modified list with delimiter inserted between consecutive elements
    """
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:  # Check if it's not the last element
            result.append(delimiter)
    return result

# Example usage:
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```
This Python script defines the `intersperse` function that takes a list of numbers and a delimiter as input and returns a new list with the delimiter inserted between every two consecutive elements of the input list. The function uses a for loop with `enumerate` to iterate over the input list, appending each number to the result list and then appending the delimiter if it's not the last element. The example usage demonstrates the function's behavior with an empty list and a list of numbers.