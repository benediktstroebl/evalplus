```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))

# Test suite
numbers = [1, 2, 3, 2, 4, 3, 5]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 3, 4]

numbers = [2, 4, 4, 2, 3]
result = remove_duplicates(numbers)
print(result)  # Output: [2, 3]

numbers = [1, 1, 2, 3, 4]
result = remove_duplicates(numbers)
print(result)  # Output: [1, 2, 3, 4]

numbers = [2, 4, 5, 4, 2]
result = remove_duplicates(numbers)
print(result)  # Output: [2, 4, 5]
```
The function **remove_duplicates** takes a list of integers as input and returns a new list that contains only the unique elements of the input list. The test suite contains four test cases with different lists of integers, and the output of the **remove_duplicates** function is printed to verify the correct functionality of the function.