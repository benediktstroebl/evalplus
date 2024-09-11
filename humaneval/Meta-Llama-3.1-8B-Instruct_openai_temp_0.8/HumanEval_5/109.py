```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`.

    Args:
    numbers (List[int]): The input list of integers.
    delimeter (int): The number to be inserted between consecutive elements.

    Returns:
    List[int]: The list with the delimeter inserted between every two consecutive elements.
    """
    if not numbers:  # if the input list is empty, return an empty list
        return []

    result = [numbers[0]]  # start with the first element of the input list
    for num in numbers[1:]:  # iterate over the rest of the input list
        result.append(delimeter)  # insert the delimeter
        result.append(num)  # append the current number

    return result


# Example usage
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([1, 2, 3, 4, 5], 0))  # [1, 0, 2, 0, 3, 0, 4, 0, 5]
```

This script uses a simple loop to go through the input list `numbers`, inserting the `delimeter` between every two consecutive elements. The `if not numbers` check at the beginning of the function is used to return an empty list when the input list is empty.