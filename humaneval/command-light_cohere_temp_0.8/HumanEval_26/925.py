Here's the provided self-contained Python function:
```python
from typing import List


def remove_duplicates(numbers: List[int]):
    # Initialize a set to store unique integers
    unique_numbers = set()
    
    # Convert the input list into a set of integers
    for num in numbers:
        unique_numbers.add(num)
    
    # Return a list of unique integers
    return list(unique_numbers)
```
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with all distinct integers. The function uses the `set` to convert the input list into a set, then iterates through the original list, adding each integer to the set if it's not already present. Finally, the function returns the list of unique integers from the set.

This function is self-contained, it does not require any additional imports or external functions. It can be easily used to solve the given problem and pass the tests.