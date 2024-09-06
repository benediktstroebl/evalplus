```python
from typing import List
def remove_duplicates(numbers: List[int]):
    # Initialize a set to store unique numbers
    duplicates = set()
    result = []
    for num in numbers:
        if num not in duplicates:
            duplicates.add(num)
            result.append(num)
   return list(result)
# Test cases
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Expected output: [1, 3, 4]
numbers = [5, 5, 5, 5]
print(remove_duplicates(numbers))  # Expected output: [5, 5, 5]
```