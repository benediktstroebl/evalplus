```python
from typing import List
def remove_duplicates(numbers: List[int]):
    # Initialize an empty set to store unique integers
    unique_ints = set()

    # Iterate through the list of integers
    for num in numbers:
        # If the number is already in the set, it's a duplicate, so we add it again
        if num in unique_ints:
            unique_ints.add(num)
        # Otherwise, otherwise, add it to the set
        else:
            unique_ints.add(num)

    # Return the list of unique integers from the set
    return [num for num in unique_ints]

# Unit tests
numbers = [1, 2, 3, 2, 4, 3, 5]
assert remove_duplicates(numbers) == [1, 2, 3, 4, 5]

numbers = [6, 9, 2, 3, 6, 9]
assert remove_duplicates(numbers) == [6, 9, 2]

numbers = [1, 2, 3, 3, 4, 5, 6]
assert remove_duplicates(numbers) == [1, 2, 3, 4, 5]
```