```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in set(numbers)]


# Test cases
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Expected output: [1, 3, 4]

numbers = [3, 2, 4, 2, 1]
print(remove_duplicates(numbers))  # Expected output: [1, 3, 4]

numbers = [4, 2, 1]
print(remove_duplicates(numbers))  # Expected output: [1, 4]

numbers = [1, 1, 2]
print(remove_duplicates(numbers))  # Expected output: [1, 2]

numbers = [1, 2, 3, 4, 5]
print(remove_duplicates(numbers))  # Expected output: [1, 2, 3, 4]
```

This Python code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with duplicate elements removed. The function utilizes the important type hint `List[int]` to the input parameter `numbers`. It then employs the built-in `set` function to create a set of unique elements from the input list. Finally, the function employs a list comprehension to filter out the duplicate elements from the input list, returning the list with unique integers.