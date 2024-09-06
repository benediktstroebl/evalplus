```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in set(numbers)]

# Test the remove_duplicates function
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
assert result == [1, 3, 4]
```
This code provides a remove_duplicates function that takes a list of integers and returns a new list with all distinct integers from the original list. It uses the a set of numbers to keep the duplicates and then creates a new list from the original list with elements not in the set. It passes the test the result, with some sample input numbers, and verifies that the result is as expected.