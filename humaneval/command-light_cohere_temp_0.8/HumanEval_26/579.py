```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize an empty set
    duplicates = set()

    # Initialize an empty result list
    result = []

    # Loop through the input list
    for num in numbers:
        if num not in duplicates:
            duplicates.add(num)
            result.append(num)

    return result
```
This code defines a function called `remove_duplicates`, which takes a list of integers as input and returns a new list with any duplicate numbers removed. The function uses a set data structure to keep track of duplicate numbers and creates a new list with the remaining unique elements. This is a `duplicates` set, and every time a number is encountered in the list for the first time, it is added to the `duplicates` set. The function then appends the duplicates from the set to the result list and returns the new list.