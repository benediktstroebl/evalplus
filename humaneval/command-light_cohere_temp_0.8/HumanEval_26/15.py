```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Create a set to store unique numbers
    unique_numbers = set(numbers)

    # Convert the set back into a list
    result = list(unique_numbers)
    return result

# Test cases
numbers_list = [1, 2, 3, 2, 4, 3, 1, 4]
result_from_test = remove_duplicates(numbers_list)
print(f"Result from test: {result_from_test}")

numbers_list2 = [4, 1, 2, 3]
result_from_new_test = remove_duplicates(numbers_list2)
print(f"Result from new test: {result_from_new_test}")
```

This script defines a function called `remove_duplicates`, which takes a list of integers as input and returns a new list with all unique elements. It uses the use of a `set` data structure to store unique numbers, and then converts it back to a list. This function effectively removes all duplicate elements from the input list.

The script also provides two test cases: it creates a list of integers, then calls the `remove_duplicates` function on this list, and prints the resulting list. This process is expected to print the unique elements from the input list.