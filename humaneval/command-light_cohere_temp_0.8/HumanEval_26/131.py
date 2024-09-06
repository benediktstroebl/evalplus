```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [num for num in numbers if num not in seen and num not in [2] + seen]
    return result

# Unit tests
numbers = [1, 2, 3, 2, 4]
test_remove_duplicates = [
    'This is a duplicate!',
    2, 4, 3, 1, 2  # Changed to not be duplicate
]
result = remove_duplicates(numbers)
test_remove_duplicates[0]  # This should return 2, not changed
test_remove_duplicates[1]  # This should be 3, not changed
test_remove_duplicates[2]  # This should be 4, not changed
test_remove_duplicates[3]  # This should be 2, not changed
test_remove_duplicates[4]  # This should be 1, not changed

print(result == test_remove_duplicates)
``` 
This script provides a function `remove_duplicates` that accepts a list of integers and outputs a list of integers that are unique. The script also provides a set of numbers to test this function with.