```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize an empty list to store unique numbers
    result = []
    for num in numbers:
        if num not in result:
            result.append(num)
    return result

# Unit tests for the remove_duplicates function
numbers_list = [1, 2, 3, 2, 4, 3, 1, 4]
result_from_input = remove_duplicates(numbers_list)

# Test if the function correctly removes duplicates
same_numbers = [1, 2, 2, 2]
duplicates = remove_duplicates(same_numbers)
assert len(duplicates) == 2, "Function did not remove duplicates as expected"

# Test if the function works correctly with a list of different numbers
numbers_list_diff = [1, 2, 3, 4]
result_from_diff = remove_duplicates(numbers_list_diff)
assert len(result_from_diff) == 4, "Function did not remove the correct duplicates"
```
This code defines a function called remove_duplicates, which removes duplicate integers from a list. The function iterates through the test cases, passing all the tests successfully.