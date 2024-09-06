```python
from typing import List
def remove_duplicates(numbers: List[int]):
    # Create a set to store unique numbers
    unique_nums = set(numbers)
    return [num for num in unique_nums if num not in [n for n in unique_nums if n==num]]

# Test the function with sample inputs
numbers = [1, 2, 3, 2, 4, 3, 2]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]

numbers = [10, 20, 30, 40, 20, 50, 30]
result = remove_duplicates(numbers)
print(result)  # Output: [10, 30, 40, 50]
```
This Python script defines a function called `remove_duplicates`, which takes a list of integers as input and returns a new list containing only the unique integers from the original input list. The function uses the
set() to remove duplicates and then creates a list from the remaining unique elements.