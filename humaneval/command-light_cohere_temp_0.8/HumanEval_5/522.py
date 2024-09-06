Here's a self-contained Python function that solves the markdown code block problem:
```python
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Insert a number 'delimiter' between every two consecutive elements of the input list.
    The
    list of integers is split into chunks of 2 elements, and the
    next value in the chunk becomes the delimiter.
    >>>  example:
    numbers = [1, 2, 3, 4, 5]
    delimeter = 2
    result = [1, 2, 3, 4, 5]
    -> [1, 2, delimeter, 4, 5]
    -> [1, 2, 5, 4, 5]
    """
    return [i + delimeter for i, i+delimeter[1:] for i, delimeter in zip(numbers, List(delimeter))]
```

This function efficiently solves the problem of inserting a number 'delimiter' between every two consecutive elements of the input list 'numbers'.  The function uses list comprehension to iterate over the list and create new lists with the desired structure.  The list comprehension creates a new list by applying the specified transformation to each element in the input list.  The final result is a list of lists with the original numbers and the inserted delimiter in between.