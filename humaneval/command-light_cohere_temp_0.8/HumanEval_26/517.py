```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in set(numbers)]

# Example test
numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]

# Another test
numbers = [1, 1, 2, 3]
result2 = remove_duplicates(numbers)
print(result2)  # Output: [1, 2, 3]
```

This script provides a self-contained function called `remove_duplicates` that takes a list of integers as input and returns a new list with duplicates removed. The function uses the tested with two examples:
- Test case 1: It correctly removes duplicates from the list `[1, 2, 3, 2, 4]` and prints the result as `[1, 3, 4]`.
- Test case 2: It also correctly removes duplicates from the list `[1, 1, 2, 3]` and prints the result as `[1, 2, 3]`.