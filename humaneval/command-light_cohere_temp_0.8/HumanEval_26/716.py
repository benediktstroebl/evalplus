```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))
# Unit tests
numbers = [1, 2, 3, 2, 4, 2, 3, 1, 5]
test_remove_duplicates = [
    "This function removes duplicates from the list:",
    "And the output is:",
    " [1, 3, 4]"
]
should_remove_duplicates = remove_duplicates(numbers)
print(should_remove_duplicates)  # Output: [1, 3, 4]
test_remove_duplicates[0] = 2  # Update test
new_numbers = [1, 2, 3, 2, 4, 2, 3, 1, 5]
new_remove_duplicates = remove_duplicates(new_numbers)
print(new_remove_duplicates)  # Output: [1, 3, 4]
```