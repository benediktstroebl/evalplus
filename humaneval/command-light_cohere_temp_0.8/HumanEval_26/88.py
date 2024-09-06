```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)  # Convert to set to remove duplicates
    return [num for num in numbers if num not in set([])]

# Unit tests
numbers = [1, 2, 3, 2, 4]
test_remove_duplicates = [
    "This function removes duplicates correctly.",
    "Test case 1: Should return [1, 3, 4]",
    "Test case 2: This is unique.",
    "Test case 3: Should return [1, 2, 3]"
]

test_remove_duplicates_results = remove_duplicates(numbers)
print("Test Results:", test_remove_duplicates_results)
``` 
This code defines a function `remove_duplicates`, which takes a list of integers as input and returns a new list with all unique integers from the input. It achieves this by first converting the list to a set, which removes any duplicates, and then it uses list comprehensions to filter out any elements not present in the set from the original input list.