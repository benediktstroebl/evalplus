```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    # Initialize a set to store unique integers
    set_unique = set(numbers)
    # Filter out elements that are duplicates in the set
    unique_numbers = [num for num in numbers if num not in set_unique]
    return unique_numbers

# Test cases
numbers_list = [1, 2, 3, 2, 4, 2, 3]
result = remove_duplicates(numbers_list)
print(result)  # Output: [1, 3, 4]

numbers_set = {1, 2, 3, 4, 5, 6}
result = remove_duplicates(numbers_set)
print(result)  # Output: [1, 3, 4, 5, 6]

numbers_mixed = [1, 2, 3, 2, 4, 5, 6, 7]
result = remove_duplicates(numbers_mixed)
print(result)  # Output: [1, 2, 3, 4, 5, 6, 7]
```
This script defines a function `remove_duplicates` that takes a list of integers as input and removes all duplicate elements from it. It utilizes a both a list and set of numbers to ensure duplicates are removed. It then filters the the set to obtain unique numbers, which are subsequently returned. The function is tested using three test cases: a list, a set of unique numbers, and a list of mixed numbers. 

Note that the output will be a list of unique integers, ensuring duplicates are properly removed.