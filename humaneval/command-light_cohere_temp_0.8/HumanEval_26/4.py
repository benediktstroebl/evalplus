Here's a Python script that includes the function `remove_duplicates` with a detailed explanation:

```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove all duplicates from a list of integers and return the unique elements.
    >>
    By default, the function will use the input list of integers and return the list of unique integers.
    """
    number of unique elements in the list is returned as the function's output.
    """
    function uses a type List[int] in the numbers parameter and the list of integers that don't occur more than once in the input list.
    """
    input:
    numbers: List[int]
    output: List[int]
    """
    unique_numbers = set(numbers)
    return list(unique_numbers)
```

The provided solution employs the `set()` function to convert the input list of integers into a set. The `set()` function effectively eliminates duplicate elements by converting the input into a unique set of integers. This set serves as a unique and distinct representation of the input integers, eliminating any duplicates. The function then employs the `list()` function to convert the set back into a list, which is subsequently returned as the output of the function.

This approach ensures the removal of duplicates from the input list, while efficiently utilizing set data structures to achieve this. It effectively addresses the value in the problem of eliminating duplicates and provides a clear and concise solution using set principles.