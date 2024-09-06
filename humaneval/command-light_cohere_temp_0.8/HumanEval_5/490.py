Here is a Python script that includes the function `intersperse()`:
```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list `numbers`.

    Parameters:
        numbers (List[int]): List of integers
        delimiter (int): Integer to insert as separator

    Returns:
        List[int]: List of integers with separators inserted
    """
    new_list = []
    for num in numbers:
        new_list.append(num)
        new_list.append(delimiter)
        new_list.append(num)
    return new_list
```

This script defines a function `intersperse()` that inserts a specified integer `delimiter` between every two consecutive elements of a given list `numbers`. The function takes two arguments: `numbers`, which is the input list of integers, and `delimiter`, which is the integer to be inserted between each pair of consecutive elements. The function creates a list `new_list` and iterates through the `numbers` list, appending each integer to the list, then inserting the `delimeter` and back the same integer. The function then appends the list to the `new_list` and returns the resulting list.