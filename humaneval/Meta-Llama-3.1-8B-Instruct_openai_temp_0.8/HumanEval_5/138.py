```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`

    Args:
        numbers (List[int]): The list of numbers
        delimeter (int): The number to be inserted between elements

    Returns:
        List[int]: The list with 'delimeter' inserted between elements
    """
    if not numbers:  # if input list is empty
        return []
    
    result = [numbers[0]]  # start with the first element
    for num in numbers[1:]:  # loop through the rest of the list
        result.extend([delimeter, num])  # append 'delimeter' and then 'num' to the result list
    return result

# Example usage:
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This Python script defines the `intersperse` function as per the problem description. It checks for an empty input list and handles it accordingly. The function then iterates through the rest of the list, inserting the 'delimeter' before each element and extending the result list. The example usage at the end demonstrates how to use the function with different inputs.