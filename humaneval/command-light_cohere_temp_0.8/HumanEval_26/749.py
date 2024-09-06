```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize a set to store unique integers.
    set_numbers = set()
    # Loop through the list and add integers to the set
    for num in numbers:
        set_numbers.add(num)
    # After the loop, return the list of elements that are in the set
    return list(set_numbers)
```