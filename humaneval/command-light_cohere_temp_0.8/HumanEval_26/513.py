```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))

numbers = [1, 2, 3, 2, 4]
result = remove_duplicates(numbers)
print(result)
```

This function, remove_duplicates, accepts a list of integers as an argument and outputs a new list where all duplicate numbers have been removed. The process is done by converting the input list into a set and then back into a list, effectively eliminating all duplicates.