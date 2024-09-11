```python
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'
    
    Args:
    numbers (List[int]): The input list of integers
    delimiter (int): The number to insert between elements
    
    Returns:
    List[int]: The modified list with the delimiter inserted
    """
    
    if not numbers:  # if the input list is empty
        return numbers
    
    result = [numbers[0]]  # initialize the result list with the first element of the input list
    
    for num in numbers[1:]:  # iterate over the rest of the input list
        result.append(delimiter)  # add the delimiter to the result list
        result.append(num)  # add the current number to the result list
    
    return result


# Example usage:
if __name__ == "__main__":
    print(intersperse([], 4))  # Test case: empty list
    print(intersperse([1, 2, 3], 4))  # Test case: non-empty list
```

This script defines a function `intersperse` that takes a list of integers and a delimiter integer as input, and returns a new list where the delimiter is inserted between every two consecutive elements of the input list. The function uses a simple iterative approach to build the result list.

The `if __name__ == "__main__":` block includes example usage of the `intersperse` function, demonstrating its behavior with an empty list and a non-empty list.