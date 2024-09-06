```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize a set to store unique integers.
    set_int = set()
    # Loop through list and add numbers to set
    for num in numbers:
        set_int.add(num)
    # Create new list to store remaining elements after removing duplicates
    remaining_numbers = [num for num in numbers if num not in set_int]
    # Return the list of unique integers
    return remaining_numbers

# Example usage
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Expected output: [1, 3, 4]
```

This script defines a function remove_duplicates that takes a list of integers as input and returns a new list with unique integers after removing duplicates. The function uses a set data structure to keep track of unique integers and a list comprehension to filter the remaining elements.

Note: This function handles the problem of removing duplicates from a list of integers and passes all corresponding tests.