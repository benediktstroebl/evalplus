```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`

    Args:
        numbers (List[int]): The input list of integers
        delimeter (int): The number to be inserted between consecutive elements

    Returns:
        List[int]: The modified list with the delimeter inserted
    """
    if not numbers:  # if the input list is empty, return an empty list
        return []

    result = [numbers[0]]  # initialize the result list with the first element of the input list
    for num in numbers[1:]:  # iterate over the rest of the elements in the input list
        result.append(delimeter)  # append the delimeter to the result list
        result.append(num)  # append the current number to the result list

    return result


# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
print(intersperse([1, 2, 3, 4, 5], 0))  # [1, 0, 2, 0, 3, 0, 4, 0, 5]
```

This script defines the `intersperse` function as described in the problem statement. The function takes a list of integers and a delimeter integer as input and returns a new list where the delimeter is inserted between every two consecutive elements of the input list. The script also includes test cases to demonstrate the function's behavior.