```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Remove duplicates from a list of integers.
    Input: numbers: List[int]
    Output: List[int]
    """
    # Initialize Set
    duplicates = set()

    # Initialize output list
    result = []

    # Loop through list
    for num in numbers:
        if num not in duplicates:
            duplicates.add(num)
            result.append(num)

    return result
```

This code implements a remove_duplicates function that takes a list of integers as input and returns a new list with duplicate values removed. The function utilizes a set to keep track of duplicate values and then loops through the input list, appending only the values that are not already present in the set. The function returns the result list with values that haven't been duplicates.