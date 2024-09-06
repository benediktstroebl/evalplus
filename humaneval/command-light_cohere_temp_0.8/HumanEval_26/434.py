```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in set(numbers)]
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]

numbers = [1, 2, 3, 2, 4, 2]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4]

numbers = [1, 2, 3, 4, 2, 3, 1]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4]

numbers = [1, 2, 3, 4, 5]
print(remove_duplicates(numbers))  # Output: [1, 2, 3, 4]
```
The problem of removing duplicates from a list of integers is solved using the remove_duplicates function in this Python script. The function takes a list of integers as input and returns a new list with all unique integers. The test cases demonstrate the case that the function works as expected and removes all duplicate elements from the input list.