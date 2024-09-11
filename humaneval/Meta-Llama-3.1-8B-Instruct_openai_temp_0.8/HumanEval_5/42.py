```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of integers.
        delimeter (int): The integer to insert between consecutive elements.

    Returns:
        List[int]: The modified list with the delimeter inserted.
    """
    if not numbers:  # If the input list is empty, return it as is
        return numbers

    result = [numbers[0]]  # Start with the first element
    for num in numbers[1:]:  # Iterate over the rest of the list
        result.append(delimeter)  # Insert the delimeter
        result.append(num)  # Append the current number

    return result


# Example usage
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines the `intersperse` function as specified and provides an example usage at the end. The function works by iterating over the input list, appending the delimeter and the current number to the result list for each iteration. If the input list is empty, it simply returns the empty list.