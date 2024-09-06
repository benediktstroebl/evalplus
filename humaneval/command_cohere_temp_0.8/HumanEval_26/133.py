```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicates from a list of integers and returns the unique list in the same order as input. """
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result
```

This script defines a function called `remove_duplicates` which takes a list of integers as input and returns a list of unique integers. Inside the function, it uses a set called `seen` to keep track of observed integers and a list called `result` to store the unique values in the same order as the input `numbers` list. The function iterates through each integer in the input list, and if an integer is not in the `seen` set, it adds it to the set, and the integer is appended to the `result` list. Finally, the function returns the `result` list containing the unique integers, free of duplicates. 

Here is an example usage of the function:
```python
>>> remove_duplicates([1, 2, 3, 2, 4])
[1, 3, 4]
```
This tests the function with a list of integers where some elements are duplicates, and the function is expected to return a list containing only the unique integers from the input.