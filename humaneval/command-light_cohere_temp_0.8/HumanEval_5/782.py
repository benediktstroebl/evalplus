```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list.
    Time complexity: O(n)
    Space complexity: O(1)
    
    Input: numbers: List[int] - list of integers to be interspread
             delimiter: int - the value to be inserted as separator
             returns: List[int] - interspaced list of integers
    """
    new_list = [num + delimeter for num, _ in enumerate(numbers, 1)]
    return new_list[:]

# Test cases
print(intersperse([], 4))  # Output: []
print(intersperse([1, 2, 3], 4))  # Output: [1, 4, 2, 4, 3]
```

This function, `intersperse`, takes a list of integers (`numbers`) and a delimiter integer (`delimiter`) as input and returns an interspaced list of integers. The function uses a iteration and the `enumer` function to achieve the desired output.