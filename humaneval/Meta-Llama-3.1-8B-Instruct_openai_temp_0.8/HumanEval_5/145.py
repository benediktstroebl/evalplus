```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of integers.
        delimeter (int): The number to be inserted between the input list elements.

    Returns:
        List[int]: The modified list with the delimeter inserted between elements.

    Example:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:  # Check if the list is empty
        return []
    result = [numbers[0]]  # Start with the first element of the list
    for num in numbers[1:]:  # Iterate over the rest of the list
        result.append(delimeter)  # Insert the delimeter
        result.append(num)  # Append the current element
    return result

# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

In this script, we define a function `intersperse` that takes two arguments: `numbers` (a list of integers) and `delimeter` (an integer). We use a simple iterative approach to build the result list by inserting the delimeter between each pair of consecutive elements from the input list. We also include test cases to demonstrate the function's behavior.