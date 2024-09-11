```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    
    Args:
        numbers (List[int]): The input list of integers
        delimeter (int): The integer to insert between every two elements
    
    Returns:
        List[int]: The modified list with the delimiter inserted
    """
    if not numbers:  # if the list is empty, return it as is
        return numbers
    
    result = [numbers[0]]  # start with the first element
    
    for num in numbers[1:]:  # iterate over the rest of the list
        result.append(delimeter)  # insert the delimiter
        result.append(num)  # append the current number
    
    return result

# Example use cases
if __name__ == "__main__":
    print(intersperse([], 4))  # []
    print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
    print(intersperse([1, 2, 3, 4, 5], 0))  # [1, 0, 2, 0, 3, 0, 4, 0, 5]
```

This script defines a function `intersperse` that inserts a specified delimiter between every two consecutive elements of an input list. The function uses a simple iterative approach to achieve this. It first handles the edge case where the input list is empty. Then, it iterates over the input list (starting from the second element, since the first element is already included in the initial result list), inserting the delimiter and appending the current number to the result list. Finally, the function returns the modified list. The example use cases demonstrate the function's behavior on different inputs.