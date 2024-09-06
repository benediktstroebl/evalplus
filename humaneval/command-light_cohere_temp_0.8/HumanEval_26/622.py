```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))
# Unit tests
numbers_list = [1, 2, 3, 2, 4, 2, 3, 5]
remove_duplicates_result = remove_duplicates(numbers_list)
print(remove_duplicates_result) # Output: [1, 2, 3, 4, 5]
```
This script defines a function `remove_duplicates` that takes a list of integers as input and returns a new list with no duplicates. The output will be a set of integers, in this case `[1, 2, 3, 4, 5]`.