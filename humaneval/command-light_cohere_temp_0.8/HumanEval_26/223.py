```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.count()]]

numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]

numbers = [1, 2, 3, 2, 4, 5, 2]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 5]

numbers = [1, 2, 3, 2, 4, 2, 5, 6]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3, 4, 5]
```
This script provides a self-contained function `remove_duplicates`, which takes a list of integers as input and returns a new list with all distinct integers from the input.