```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
    numbers (List[int]): The list of integers to be modified.
    delimeter (int): The number to be inserted between the elements.

    Returns:
    List[int]: The modified list with the delimeter inserted between every two consecutive elements.
    """
    if not numbers:
        # If the input list is empty, return the empty list
        return []

    result = [numbers[0]]  # Start with the first element
    for num in numbers[1:]:  # Iterate over the rest of the list
        result.append(delimeter)  # Append the delimeter
        result.append(num)  # Append the current number

    return result

# Test the function
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```
In this code, we start with the first element of the input list, and then in each iteration of the loop, we append the delimeter followed by the current number to the result list. This effectively inserts the delimeter between every two consecutive elements of the input list.