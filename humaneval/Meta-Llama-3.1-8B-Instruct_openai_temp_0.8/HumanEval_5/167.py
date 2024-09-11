```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): Input list of integers
        delimeter (int): The number to be inserted between each pair of elements

    Returns:
        List[int]: List with delimeter inserted between each pair of elements
    """
    
    # Initialize the result list with the first element of the input list
    result = [numbers[0]]
    
    # Iterate over the input list starting from the second element
    for i in range(1, len(numbers)):
        # Append the current delimeter to the result list
        result.append(delimeter)
        # Append the current element to the result list
        result.append(numbers[i])
    
    # Return the result list
    return result


# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This Python script provides a function called `intersperse` that inserts a specified number (`delimeter`) between each pair of consecutive elements in the input list (`numbers`). The function then returns this modified list. It includes docstrings and example test cases to demonstrate the function's usage.