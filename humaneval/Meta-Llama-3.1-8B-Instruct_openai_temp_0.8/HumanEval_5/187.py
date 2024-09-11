```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`

    Args:
        numbers (List[int]): The input list of integers
        delimeter (int): The number to be inserted between each pair of consecutive elements

    Returns:
        List[int]: The modified list with the delimeter inserted between each pair of consecutive elements
    """
    if not numbers:  # if the list is empty, return it as is
        return numbers
    result = [numbers[0]]  # start with the first element of the list
    for num in numbers[1:]:  # iterate over the rest of the list
        result.append(delimeter)  # insert the delimeter before each element
        result.append(num)
    return result


# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines the `intersperse` function, which inserts a specified number between every pair of consecutive elements in the input list. It handles the case where the input list is empty and includes test cases to verify its correctness.