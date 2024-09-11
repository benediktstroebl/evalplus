### Interspersing Elements in a List
```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`

    Args:
        numbers (List[int]): Input list of integers
        delimeter (int): Integer to be inserted between list elements

    Returns:
        List[int]: List with delimeter inserted between every two consecutive elements
    """
    if not numbers:  # Check if input list is empty
        return []

    result = [numbers[0]]  # Start with the first element of the list
    for num in numbers[1:]:  # Iterate over the rest of the list
        result.append(delimeter)  # Insert delimeter before each element
        result.append(num)
    return result[:-1]  # Remove the extra delimeter at the end

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```
This script uses a simple iterative approach to insert the delimeter between every two consecutive elements in the input list. The function `intersperse` takes two parameters: the input list `numbers` and the delimeter `delimeter`. If the input list is empty, it returns an empty list. Otherwise, it starts by appending the first element of the list to the result list, then iterates over the rest of the list, appending the delimeter and each element in turn. Finally, it removes the extra delimeter at the end of the result list before returning it.