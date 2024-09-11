```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'.

    Args:
    numbers (List[int]): Input list of integers
    delimiter (int): Number to be inserted between consecutive elements

    Returns:
    List[int]: Modified list with delimiter inserted between elements
    """
    if not numbers:  # if input list is empty
        return numbers
    
    result = [numbers[0]]  # initialize result list with first element of input list
    for i in range(1, len(numbers)):  # iterate over the input list starting from second element
        result.append(delimiter)  # add delimiter to the result list
        result.append(numbers[i])  # add current element to the result list
    
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that inserts a specified number `delimiter` between every two consecutive elements of the input list `numbers`. The function handles the edge case where the input list is empty and returns the modified list with the delimiter inserted between elements. The test cases verify the correctness of the function.