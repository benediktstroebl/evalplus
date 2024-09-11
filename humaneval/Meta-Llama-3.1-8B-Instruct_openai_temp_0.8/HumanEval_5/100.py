```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    
    Args:
    numbers (List[int]): Input list of integers
    delimeter (int): The number to be inserted between every two elements

    Returns:
    List[int]: A new list with the delimeter inserted between every two elements
    """
    if not numbers:  # edge case: if input list is empty
        return []
    
    result = [numbers[0]]  # initialize result list with the first element
    
    for num in numbers[1:]:  # loop through the rest of the list
        result.append(delimeter)  # add the delimeter
        result.append(num)  # add the current number
    
    return result


# Example usage:
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This Python script defines a function `intersperse` that takes in a list of integers and a delimeter integer. It returns a new list where the delimeter is inserted between every two consecutive elements of the input list. The function handles the edge case where the input list is empty and uses a loop to construct the result list. The example usage shows how to use the function with different inputs.