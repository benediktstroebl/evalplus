```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimiter' between every two consecutive elements of input list.
    Args:
        numbers (List[int]): list of integers to be interspersed.
    Returns: a list of integers with the delimiter inserted between every two
    consecutive elements.
    """

    Input list may example:
        [1, 2, 3, 4, 5]
        -> [1, 2, 3, 4, 5, 4, 5] 
    """
    numbers.insert(delimiter, numbers[1], numbers[2])
    for i in range(3, len(numbers), 2):
        numbers.insert(delimiter, numbers[i], numbers[i+1])
    return numbers
``` 
The function takes two parameters: `numbers`, which is a list of integers, and `delimiter`, which is an integer that specifies the number of integers to insert between every two consecutive elements of the input list. 

The function then inserts the specified number of integers between every two consecutive elements of the input list. 

Finally, it returns the modified list of integers.