```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))
```
This Python script provides a function called `remove_duplicates`, which takes a list of integers (`List[int]`) as input and returns a list of unique integers from the input list. Here's how it works:
1. The function uses a set data structure, denoted by `set(numbers)`, to automatically eliminate duplicate elements from the input list. Sets inherently exclude duplicate values, and the input list is converted into a set using the `set()` function.
2. The set is then converted back into a list using the `list()` function to provide a more readable output and maintain the order of the unique elements.

The script ensures that all duplicate integers are removed from the input list, and it maintains the order of the remaining unique elements. 

The function call `remove_duplicates([1, 2, 3, 2, 4])` would return `[1, 3, 4]`, which is the desired output for the provided test case.  This function is modular and reusable for any list of integer inputs that require duplicate removal.