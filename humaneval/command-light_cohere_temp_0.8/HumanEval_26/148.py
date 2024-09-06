```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in set(numbers) if num not in numbers]

numbers = [1, 2, 3, 2, 4, 3, 1]
print(remove_duplicates(numbers))  # expected output: [1, 3, 4]

numbers = [1, 2, 2, 3, 2]
print(remove_duplicates(numbers))  # expected output: [1, 2, 3]

numbers = [1, 2, 3, 4, 3]
print(remove_duplicates(numbers))  # expected output: [1, 3, 4]

numbers = [1, 2, 4, 3, 5]
print(remove_duplicates(numbers))  # expected output: [1, 2, 4]

numbers = List[1, 1, 3, 4, 3]
print(remove_duplicates(numbers))  # expected output: [1, 3, 4]
```

The code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with elements that are not duplicate. The `set()` function is used to remove the duplicates, and the `if` statement is used to filter out the duplicate elements from the input list. 

The code then creates a test list and calls the `remove_duplicates` function to verify the expected output.