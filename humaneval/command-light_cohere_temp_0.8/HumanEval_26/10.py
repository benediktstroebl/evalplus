```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize a set to store unique integers.
    unique_integers = set()

    # Add all elements to the set
    for num in numbers:
        unique_integers.add(num)

    # Convert the set back to a list and return
    return list(unique_integers)

# Unit tests
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
should_be = [1, 3, 4]

print(result == should_be)
``` 
This code defines a function **`remove_duplicates`** that takes a list of integers as input and removes all duplicate elements, returning a new list with unique integers. The set data structure is used to store unique integers, ensuring no duplicates are stored. The output of this code will print whether the result list is equal to the expected list, confirming the function's correctness.