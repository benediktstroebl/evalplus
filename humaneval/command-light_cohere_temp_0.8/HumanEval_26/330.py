```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keeps elements from left as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    return [num for num in numbers if num not in numbers[numbers.index()]]


# Test
numbers = [1, 2, 3, 2, 4, 3, 5]
print(remove_duplicates(numbers))
```