Here is a self-contained Python script that solves the problem of removing duplicate integers from a list and tests the function's effectiveness:
```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize a set to store unique elements
    unique_elements = set(numbers)

    # Convert the set back to a list
    elements_list = list(unique_elements)

    return elements_list

# Test cases
test_data = [1, 2, 3, 2, 4, 3, 5, 6]
test_remove_duplicates = remove_duplicates(test_data)
print("Test case 1:", test_remove_duplicates)

test_data = [1, 2, 3, 2, 4, 5, 6]
test_remove_duplicates = remove_duplicates(test_data)
print("Test case 2:", test_remove_duplicates)

test_data = [1, 2, 3, 4, 5, 6, 2]
test_remove_duplicates = remove_duplicates(test_data)
print("Test case 3:", test_remove_duplicates)

test_data = [1, 2, 3, 4, 6, 5, 7]
test_remove_duplicates = remove_duplicates(test_data)
print("Test case 4:", test_remove_duplicates)
```

This script provides a `remove_duplicates` function that accepts a list of integers and returns a new list with duplicate elements removed. The test cases validate thea successful removal of duplicates from the input list, achieving a desired output.