Here is a Python script that provides a self-contained function to solve the problem of removing duplicate elements from a list of integers:
```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers]]
# Test cases
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # expected output: [1, 3, 4]

numbers = [3, 2, 4, 2, 1, 5]
print(remove_duplicates(numbers))  # expected output: [2, 1, 5]

numbers = [1, 2, 3, 4, 5, 6, 4, 3]
print(remove_duplicates(numbers))  # expected output: [1, 2, 3, 4, 5]
```
This script defines a function remove_duplicates that takes a list of integers as input and returns a new list with duplicate elements removed. The function uses a list comprehension and the not in statement to filter out duplicate elements from the input list. The provided test cases demonstrate the example usage of the function with different input lists, and the expected output is shown.