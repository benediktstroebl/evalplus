```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): Input list of integers
        delimeter (int): The number to be inserted between elements

    Returns:
        List[int]: The modified list with the delimiter inserted
    """
    if not numbers:  # if the list is empty, return it as is
        return numbers
    
    result = [numbers[0]]  # initialize the result with the first element of the list
    for num in numbers[1:]:  # loop through the rest of the list
        result.append(delimeter)  # append the delimiter
        result.append(num)  # append the current number
    return result

# Test cases
print(intersperse([], 4))
print(intersperse([1, 2, 3], 4))
```

This script defines a function `intersperse` that takes a list of integers and a delimiter as input, and returns a new list with the delimiter inserted between every two consecutive elements of the input list. If the input list is empty, the function returns the empty list as is. The script also includes test cases to verify the correctness of the function.