```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize a set to store unique numbers
    set_numbers = set()
    # Loop through the input list and add numbers to the set
    for num in numbers:
        set_numbers.add(num)
    # Create a new list with elements from the set, and return it
    return list(set_numbers)

# Unit tests
numbers_list = [1, 2, 3, 2, 4, 3, 5]
result = remove_duplicates(numbers_list)
print(result)

numbers_set = {1, 2, 3, 4, 5}
result = remove_duplicates(numbers_set)
print(result)

numbers_dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
result = remove_duplicates(numbers_dict.map)
print(result)
```

The provided code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with distinct integers. The function utilizes the process that initializes a set to store unique integers, then creates a new list by extracting elements from the set. This ensures that the elements are only duplicated if they appear in the original input list. The code also includes unit tests to verify the functionality of the `remove_duplicates` function, which should produce the expected output for different input scenarios.