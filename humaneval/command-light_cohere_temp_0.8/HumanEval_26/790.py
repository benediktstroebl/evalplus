```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Returns a same list with unique integers.
    """
    doesn't mutate the

    numbers = [1, 2, 3, 2, 4, 2, 1, 5]
    return [x for x in set(numbers) if x not in numbers]

# Test the function with different input
numbers_list = [1, 2, 3, 2, 4, 2, 1, 5, 6]
print(remove_duplicates(numbers_list))
```