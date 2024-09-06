```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in set(numbers)]
numbers = [1, 2, 3, 2, 4, 3, 4]
print(remove_duplicates(numbers))
```
This function takes a list of integers as input and returns a new list containing only the unique integers from the input. It uses the unique element set (set) to keep track of all unique elements in the input list.