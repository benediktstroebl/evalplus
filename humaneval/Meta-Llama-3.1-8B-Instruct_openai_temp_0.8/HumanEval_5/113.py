```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ 
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`

    Args:
        numbers (List[int]): A list of integers
        delimeter (int): The number to insert between consecutive elements

    Returns:
        List[int]: The modified list with the delimeter inserted
    """
    if not numbers:  # if the list is empty, return it as is
        return numbers
    result = [numbers[0]]  # start the result with the first element
    for num in numbers[1:]:  # iterate over the rest of the list
        result.append(delimeter)  # insert the delimeter
        result.append(num)  # append the current number
    return result


# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines the `intersperse` function that takes a list of integers and an integer delimeter as input. It iterates over the input list starting from the second element, inserting the delimeter and the current number into the result list. If the input list is empty, it returns the list as is. The test cases at the end verify the function's correctness.