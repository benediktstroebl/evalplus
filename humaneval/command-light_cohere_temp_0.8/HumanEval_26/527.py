```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ Removes elements that occur more than once from a list of integers.
    Input: List[int]
    Output: List[int]
    """
    return [num for num in numbers if num not in set(numbers)]


# Test case 1
numbers = [1, 2, 3, 2, 4]
print("Test case 1 passed:", numbers)

# Test case 2
numbers = [1, 2, 3, 3, 4]
print("Test case 2 passed:", numbers)

# Test case 3
numbers = [1, 2, 2, 4, 5]
print("Test case 3 passed:", numbers)
```