```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'.
    
    Args:
        numbers (List[int]): The input list of integers.
        delimeter (int): The number to insert between every two consecutive elements.

    Returns:
        List[int]: The list with 'delimeter' inserted between every two consecutive elements.
    """
    if not numbers:  # if the list is empty, return it as is
        return numbers
    result = [numbers[0]]  # start with the first element of the list
    for num in numbers[1:]:  # iterate over the rest of the list
        result.append(delimeter)  # insert the delimeter
        result.append(num)  # append the current number
    return result


# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

In this script, the `intersperse` function inserts the `delimeter` between every two consecutive elements of the `numbers` list. If the input list is empty, the function returns it as is. Otherwise, it starts with the first element of the list, then iterates over the rest of the list, inserting the `delimeter` and the current number after each iteration. The result is a new list with the `delimeter` inserted between every two consecutive elements.