```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): The input list of integers
        delimeter (int): The number to insert between consecutive elements

    Returns:
        List[int]: The modified list with the delimeter inserted
    """
    result = []
    for i, num in enumerate(numbers):
        # Append the current number to the result list
        result.append(num)
        # If it's not the last element in the list, append the delimeter
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result

# Example usage:
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and a delimeter number as input, and returns a new list with the delimeter inserted between every two consecutive elements. The function iterates over the input list using `enumerate`, which provides both the index and value of each element. It appends each element to the result list, and if it's not the last element, it also appends the delimeter. The function then returns the modified list. The script includes example usage to demonstrate the function's behavior.