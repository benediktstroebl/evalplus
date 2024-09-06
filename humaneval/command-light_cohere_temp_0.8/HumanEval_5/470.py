```python
from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimiter' between every two consecutive elements of input list. """

   
   
    list of lists, like a flat list of lists.
    """ The delimeter is used as the delimiter.
    >>> intersperse([1, 2, 3, 4], 5)
    [1, 5, 2, 5, 3]
    """
    new_list = []
    for i in numbers:
        if i != numbers[-1]:
            new_list.append(i)
        new_list.append(delimiter)
        new_list.append(i)
    new_list.append(numbers[-1])
    return new_list

This function, `intersperse`, takes a list of integers, `numbers`, and a positive integer, `delimiter`, as input. It returns a a list of lists, where the elements of every other list are separated by the `delimiter`.