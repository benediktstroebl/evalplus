```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`.
    
    Args:
    numbers (List[int]): The input list of integers.
    delimeter (int): The number to be inserted between the elements.
    
    Returns:
    List[int]: The modified list with the delimeter inserted.
    """
    if not numbers:  # if the input list is empty
        return []
    
    result = [numbers[0]]  # start with the first element of the list
    for i in range(1, len(numbers)):  # loop through the rest of the list
        result.append(delimeter)  # insert the delimeter before each element
        result.append(numbers[i])  # append the current element
    return result

# Example usage:
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```