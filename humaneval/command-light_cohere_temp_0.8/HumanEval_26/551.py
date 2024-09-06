```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes duplicate integers from a list.
    Args:
        numbers: list of integers
    Returns: list of unique integers
    """
    return [num for num in set(numbers) if num not in numbers]

# Example test cases
numbers1 = [1, 2, 3, 2]
numbers2 = [1, 2, 3, 4, 5, 6]
print("Results:", remove_duplicates(numbers1), remove_duplicates(numbers2))
```
This script defines a function called remove_duplicates that takes a list of integers as input and returns a new list with unique integers. It utilizes the using the relevant set and list comprehension to remove any duplicate elements from the input list.