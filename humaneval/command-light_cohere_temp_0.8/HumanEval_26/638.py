```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)
    return list(numbers)


def test_remove_duplicates(numbers: List[int]) -> None:
    removed_numbers = remove_duplicates(numbers)
    if not removed_numbers:
        raise ValueError("Input list is empty")
    return removed_numbers


# Example usage:
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
test_remove_duplicates(numbers)  # This will raise ValueError if empty input list
```
This script defines a `remove_duplicates` function that removes duplicate elements from a given list. The `test_remove_duplicates` function tests this function with an example list and ensures that the input list is not empty.  The list is converted into a set to remove duplicates, and then the set's elements are converted back into a list to return the unique elements.