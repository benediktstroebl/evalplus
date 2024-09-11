```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`
    
    Args:
        numbers (List[int]): The input list of integers
        delimeter (int): The number to insert between the input list elements
    
    Returns:
        List[int]: The modified list with the delimeter inserted
    """
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the input list with an index
    for i in range(len(numbers)):
        # Append the current element to the result list
        result.append(numbers[i])
        
        # If it's not the last element, append the delimeter
        if i < len(numbers) - 1:
            result.append(delimeter)
    
    # Return the modified list
    return result


# Example usage
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

In this script, the `intersperse` function iterates over the input list, appending each element followed by the delimeter (except for the last element). The result is a new list with the delimeter inserted between each pair of consecutive elements. The example usage demonstrates the function's behavior with two test cases.