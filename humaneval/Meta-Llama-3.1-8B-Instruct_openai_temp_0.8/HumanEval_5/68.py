```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`
    
    Args:
    numbers (List[int]): The list of integers to be interspersed.
    delimeter (int): The number to be inserted between every two consecutive elements.

    Returns:
    List[int]: The list of integers with the delimeter inserted between every two consecutive elements.
    """
    if not numbers:  # Check if the input list is empty
        return []
    
    result = [numbers[0]]  # Initialize the result list with the first element of the input list
    for num in numbers[1:]:  # Iterate over the rest of the elements in the input list
        result.append(delimeter)  # Append the delimeter to the result list
        result.append(num)  # Append the current element to the result list
    
    return result


# Test cases
print(intersperse([], 4))
print(intersperse([1, 2, 3], 4))
```

This script defines the `intersperse` function as specified and includes test cases to verify its correctness. The function uses a simple iterative approach to insert the delimeter between every two consecutive elements of the input list. If the input list is empty, the function returns an empty list.