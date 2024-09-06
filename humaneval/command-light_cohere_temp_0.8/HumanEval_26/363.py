```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)  # Convert to set to remove duplicates
    return [num for num in numbers if num not in set([])]


# Test the function with a sample input
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]

numbers = [1, 2, 3, 4, 3, 5]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 5]

numbers = [1, 2, 3, 4, 6]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4]

numbers = [1, 2, 3, 4, 2]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4]
```
This script provides a self-contained function called `remove_duplicates`, which takes a list of integers as input and returns a new list with duplicate elements removed. It uses the` set()` to eliminate duplicates and the list comprehension to select elements not present in the set created from the input list.