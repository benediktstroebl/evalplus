```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers`

    Args:
    numbers (List[int]): The input list of integers
    delimeter (int): The number to be inserted between every two consecutive elements

    Returns:
    List[int]: The modified list with the delimeter inserted between every two elements
    """
    if not numbers:  # check if the input list is empty
        return []
    
    result = [numbers[0]]  # initialize the result list with the first element of the input list
    
    for num in numbers[1:]:  # iterate over the rest of the elements in the input list
        result.append(delimeter)  # insert the delimeter
        result.append(num)  # append the current number
    
    return result


# Test cases
if __name__ == "__main__":
    print(intersperse([], 4))  # []
    print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
    print(intersperse([1, 2, 3, 4, 5], 0))  # [1, 0, 2, 0, 3, 0, 4, 0, 5]
```

This script defines a function `intersperse` that takes a list of integers and a delimiter as input, and returns a new list where the delimiter is inserted between every two consecutive elements. The function uses a simple iterative approach to build the result list. The test cases at the end verify that the function works correctly for different inputs.