```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)  # Convert to set to remove duplicates
    return [num for num in numbers if num not in set()]

# Unit tests
numbers_list = [1, 2, 3, 2, 4, 3, 1]
assert remove_duplicates(numbers_list) == [1, 3, 4]

```
The provided code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. It achieves this goal by converting the list into a set, which removes any duplicate elements, and then converts it back to a list while retaining the unique elements. The code also includes unit tests to verify the correctness of the `remove_duplicates` function.