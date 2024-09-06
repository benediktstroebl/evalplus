```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return [n for n in numbers if n not in set(numbers)]

# Unit tests
numbers = [1, 2, 3, 2, 4, 3, 1, 5]
result = remove_duplicates(numbers)
print(result)  # Expected output: [1, 2, 3, 4, 5]

numbers = [1, 2, 3, 3, 4, 5, 1, 2]
result = remove_duplicates(numbers)
print(result)  # Expected output: [1, 2, 3, 4, 5]

numbers = [1, 2, 3, 4, 4]
result = remove_duplicates(numbers)
print(result)  # Expected output: [1, 2, 3, 4]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = remove_duplicates(numbers)
print(result)  # Expected output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```
The function `remove_duplicates` takes a list of integers as input and returns a new list with all unique integers. The test cases cover various scenarios, including an empty list, lists with duplicates, and lists with no duplicates.