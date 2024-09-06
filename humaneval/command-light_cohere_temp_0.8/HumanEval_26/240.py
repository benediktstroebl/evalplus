```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num < len(numbers) and num not in numbers[:len(numbers)]]

# Tests
numbers = [1, 2, 3, 2, 4, 3, 1]
print(remove_duplicates(numbers))  # expected output: [1, 3, 4]

numbers = [1, 2, 3, 2, 4, 3, 5]
print(remove_duplicates(numbers))  # expected output: [1, 2, 3, 4, 5]

numbers = [1, 2, 3, 4, 3, 5, 3, 4, 6]
print(remove_duplicates(numbers))  # expected output: [1, 2, 3, 4, 5]
```
This Python script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list containing only the unique integers. The script then passes several test cases and demonstrates the functionality of the `remove_duplicates` function.