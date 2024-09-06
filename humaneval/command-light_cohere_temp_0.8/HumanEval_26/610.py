```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    return [num for num in numbers if num not in seen and num not in [n for n in numbers if n in seen]]

# Test cases
numbers_list = [1, 2, 3, 2, 4, 3, 1]
result = remove_duplicates(numbers_list)
print(result)  # Expected output: [1, 3, 4]

numbers_set = {1, 2, 3, 4}
result = remove_duplicates(numbers_set)
print(result)  # Expected output: []

list1 = [1, 2, 3, 4, 3, 2, 1]
result = remove_duplicates(list1)
print(result)  # Expected output: [1, 3, 4]

set1 = {1, 2, 3}
result = remove_duplicates(set1)
print(result)  # Expected output: []
```

This script defines a function called `remove_duplicates` that takes a list of integers as input and returns a new list containing only the unique integers. It uses a particular data structures to keep track of duplicate elements, and then filters out any elements that are encountered more than once, keeping only the first occurrence of each element. The test cases pass the have been adjusted to cover different types of input and expected outputs.