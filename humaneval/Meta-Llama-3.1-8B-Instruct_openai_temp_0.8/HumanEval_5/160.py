```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`

    Args:
        numbers (List[int]): The input list of integers
        delimeter (int): The number to insert between every two consecutive elements

    Returns:
        List[int]: The modified list with the delimiter inserted
    """
    if not numbers:  # if the list is empty, return it immediately
        return numbers
    
    result = [numbers[0]]  # start with the first element of the list
    for num in numbers[1:]:  # iterate over the rest of the list
        result.append(delimeter)  # insert the delimiter
        result.append(num)  # append the current number
    return result

# Example usage:
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and an integer delimiter as input, and returns a new list where the delimiter is inserted between every two consecutive elements of the input list. The function uses a for loop to iterate over the input list, starting from the second element (index 1), and inserts the delimiter and the current number into the result list for each iteration. If the input list is empty, the function returns the empty list immediately.