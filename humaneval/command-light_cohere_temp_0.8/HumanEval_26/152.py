```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize an empty set to store unique numbers
    duplicates = set()

    # Initialize an empty list to store the results
    result = []

    # Loop through the input list
    for num in numbers:
        if num not in duplicates:
            duplicates.add(num)
            result.append(num)

    return result
```
This function removes duplicate elements from a list of integers and returns a new list with unique integers. The function uses a set to keep track of the unique elements and a list to store the results.