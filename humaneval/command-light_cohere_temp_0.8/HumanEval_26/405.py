```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keeps elements elements left as in the input list.
    """
    numbers
    list to remove duplicates from
    """
    set(numbers) - sets(numbers)
    return numbers

# Sample Test cases:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # expected output: [1, 3, 4]

numbers = [1, 2, 3, 3, 4]
print(remove_duplicates(numbers))  # expected output: [1, 2, 3, 4]

numbers = [1, 2, 3, 4, 5]
print(remove_duplicates(numbers))  # expected output: [1, 2, 3, 4]

numbers = [1, 2, 4, 3, 1]
print(remove_duplicates(numbers))  # expected output: [1, 2, 4]

```
This script defines a function `remove_duplicates` that removes duplicate elements from a list of integers. It utilizes sets to remove duplicates and returns the modified list.