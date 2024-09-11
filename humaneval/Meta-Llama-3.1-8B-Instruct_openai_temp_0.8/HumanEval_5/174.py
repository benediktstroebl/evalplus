```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`

    Args:
        numbers (List[int]): The input list of integers
        delimeter (int): The number to insert between every two consecutive elements

    Returns:
        List[int]: The modified list with the delimeter inserted
    """
    if not numbers:  # if the list is empty
        return numbers
    result = [numbers[0]]  # start the result list with the first element
    for num in numbers[1:]:  # iterate over the rest of the list
        result.append(delimeter)  # insert the delimeter
        result.append(num)  # append the current number
    return result

# Example usage:
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```
This script uses a simple iterative approach to build the result list, inserting the delimeter between every two consecutive elements of the input list. The `if not numbers` check handles the edge case where the input list is empty.