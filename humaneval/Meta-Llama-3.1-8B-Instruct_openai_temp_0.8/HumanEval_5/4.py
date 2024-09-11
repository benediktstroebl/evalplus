```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): The input list of integers
        delimeter (int): The number to be inserted between every two consecutive elements

    Returns:
        List[int]: The list with the delimeter inserted between every two consecutive elements
    """
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if i < len(numbers) - 1:  # Check if it's not the last element
            result.append(delimeter)
    return result

# Example usage:
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

In this script, we define a function `intersperse` that takes a list of integers `numbers` and a delimeter `delimeter` as input. We then use a for loop to iterate over the elements of the input list, appending each element to the result list. After each element, we also append the delimeter to the result list, unless we are at the last element of the list. The function finally returns the resulting list.