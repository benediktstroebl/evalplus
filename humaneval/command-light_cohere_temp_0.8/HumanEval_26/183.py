Here's the self-contained Python script that solves the problem of removing duplicates from a list of integers and passes the tests:
```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize an empty set to store unique elements.
    unique_set = set()

    # Initialize an output list to store the result
    result = []

    # Loop through the input list
    for num in numbers:
        if num not in unique_set:
            unique_set.add(num)
            result.append(num)

    return result
```

This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. The function uses a set data structure to keep track of unique elements and the output list is populated with elements that are not present in the set.