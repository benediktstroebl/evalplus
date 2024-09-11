```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`

    Args:
        numbers (List[int]): The list of numbers
        delimeter (int): The number to be inserted between every two consecutive elements

    Returns:
        List[int]: The modified list with the delimeter inserted

    Example:
        >>> intersperse([], 4)
        []
        >>> intersperse([1, 2, 3], 4)
        [1, 4, 2, 4, 3]
    """
    if not numbers:  # If the list is empty, return it as is
        return numbers
    
    result = [numbers[0]]  # Initialize the result list with the first element of the input list
    for num in numbers[1:]:  # Iterate over the rest of the elements in the input list
        result.append(delimeter)  # Append the delimeter to the result list
        result.append(num)  # Append the current element to the result list
    
    return result
```

You can test this function with the provided example use cases:

```python
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```