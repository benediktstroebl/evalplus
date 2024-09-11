```python
from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of input list `numbers'

    Args:
    numbers (List[int]): A list of integers
    delimiter (int): The number to be inserted between every two consecutive elements

    Returns:
    List[int]: A new list with 'delimiter' inserted between every two consecutive elements
    """
    if not numbers:
        return []

    result = [numbers[0]]
    for num in numbers[1:]:
        result.extend([delimiter, num])

    return result


# Test cases
print(intersperse([], 4))  # []
print(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```

This script defines a function `intersperse` that takes a list of integers and a delimiter as input. It then creates a new list where the delimiter is inserted between every two consecutive elements of the input list.

The function first checks if the input list is empty. If it is, the function returns an empty list.

If the input list is not empty, the function initializes a new list `result` with the first element of the input list.

Then, for each element in the input list (except the first one), the function appends the delimiter and the current element to the `result` list.

Finally, the function returns the `result` list.

The script also includes two test cases to demonstrate the usage of the `intersperse` function.