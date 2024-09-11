### Intersperse Function
#### Inserts a specified number between every two consecutive elements of a given list.
```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
    numbers (List[int]): The input list of integers.
    delimiter (int): The number to be inserted between consecutive elements.

    Returns:
    List[int]: The list with the delimiter inserted between consecutive elements.
    """
    if not numbers:
        return []  # Return an empty list if the input list is empty
    result = [numbers[0]]  # Start with the first element of the input list
    for num in numbers[1:]:  # Iterate over the rest of the input list
        result.append(delimiter)  # Insert the delimiter before each element
        result.append(num)  # Append the current element
    return result

# Example usage
print(intersperse([], 4))  # [] (empty list)
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([5, 6, 7], 0))  # [5, 0, 6, 0, 7]
```
This script defines a function `intersperse` that takes a list of integers and a delimiter value as input, and returns a new list with the delimiter inserted between every two consecutive elements of the input list. The function first handles the case where the input list is empty, then iterates over the rest of the list, appending the delimiter and each element to the result list. Finally, it returns the result list. The example usage demonstrates the function's behavior with different input lists.