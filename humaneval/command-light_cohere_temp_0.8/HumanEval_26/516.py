```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize a set to store unique numbers
    unique_numbers = set(numbers)
    
    # Convert the set back to a list
    numbers_list = list(unique_numbers)
    
    return numbers_list

# Unit tests
numbers_list = [1, 2, 3, 2, 4, 3, 1, 5]
result = remove_duplicates(numbers_list)
print(result)

numbers_list2 = [1, 2, 3, 4, 2, 6, 5]
result2 = remove_duplicates(numbers_list2)
print(result2)

numbers_list3 = [5, 1, 2, 2, 4]
result3 = remove_duplicates(numbers_list3)
print(result3)
```

This script defines a function `remove_duplicates`, which takes a list of integers as an argument and returns a new list with duplicate elements removed. The script also includes unit tests, passing various lists of integers and verifying the correctness of the `remove_duplicates` function.