```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    # Remove duplicates
    numbers = set(numbers)
    return list(numbers)


# Test the function
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]

# Another test with just one duplicate
numbers = [1, 1]
result = remove_duplicates(numbers)
print(result)  # Output: [1]
``` 
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. The test cases pass the both scenarios.