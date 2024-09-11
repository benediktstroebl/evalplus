```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.

    Args:
        numbers (List[int]): The input list of integers.
        delimeter (int): The number to be inserted between consecutive elements.

    Returns:
        List[int]: The modified list with the delimeter inserted.
    """
    if not numbers:  # if the list is empty, return it as is
        return numbers
    
    result = [numbers[0]]  # start with the first element of the list
    for num in numbers[1:]:  # iterate over the rest of the list
        result.append(delimeter)  # add the delimeter
        result.append(num)  # add the current number
    return result


# Example usage:
print(intersperse([], 4))
print(intersperse([1, 2, 3], 4))
```