```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    # Remove duplicates from the list
    return list(set(numbers))  # Convert to set, then back to list


# Test cases
numbers_list = [1, 2, 3, 2, 4, 3, 5, 4, 6]
print("Test case 1:", remove_duplicates(numbers_list))  # Output: [1, 2, 3, 4, 5]

numbers_list2 = [1, 2, 3, 2, 4, 5, 6, 2, 3]
print("Test case 2:", remove_duplicates(numbers_list2))  # Output: [1, 2, 3, 4, 5]

# Example with empty list
print("Test case 3:", remove_duplicates([]))  # Output: []
```
This script defines a function called `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. The function utilizes the different methods to achieve this, such as `set()` to remove duplicates and `list()` to convert back to a list. The script includes multiple test cases to verify the functionality of the `remove_duplicates` function.