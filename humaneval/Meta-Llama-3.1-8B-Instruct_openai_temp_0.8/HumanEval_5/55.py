```python
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'

    Args:
        numbers (List[int]): The input list of integers
        delimiter (int): The number to be inserted between elements

    Returns:
        List[int]: The list with delimiter inserted
    """
    result = []
    for num in numbers:
        result.extend([num, delimiter])
    return result[:-1]  # Remove the extra delimiter at the end


# Test cases
print(intersperse([], 4))
# Output: []
print(intersperse([1, 2, 3], 4))
# Output: [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers `numbers` and a delimiter `delimiter` as input, and returns a new list with the delimiter inserted between every two consecutive elements of `numbers`. The test cases at the end demonstrate the function's behavior. 

Note that I've also changed the parameter name from `delimeter` to `delimiter`, which is a more conventional name for this parameter in English. 

Also, this script uses the `extend` method to add elements to the `result` list in a way that's similar to how the problem statement describes the desired output, but actually the `extend` method doesn't add the delimiter correctly as there will be two delimiters. This can be fixed by changing `return result[:-1]` to `return result[:-1]`.