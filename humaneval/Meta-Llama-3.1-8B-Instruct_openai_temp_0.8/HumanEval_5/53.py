```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
    numbers (List[int]): The input list of integers
    delimeter (int): The number to insert between elements

    Returns:
    List[int]: The list of integers with the delimeter inserted
    """
    if not numbers:  # if the list is empty, return it as is
        return numbers

    result = [numbers[0]]  # start with the first element
    for i in range(1, len(numbers)):  # iterate over the rest of the list
        result.append(delimeter)  # insert the delimeter
        result.append(numbers[i])  # append the current element
    return result

# Example usage:
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers `numbers` and a number `delimeter` as input. It returns a new list where the `delimeter` is inserted between every two consecutive elements of the input list. If the input list is empty, it returns the empty list as is. Otherwise, it starts with the first element, then iterates over the rest of the list, inserting the delimeter and the current element at each step.