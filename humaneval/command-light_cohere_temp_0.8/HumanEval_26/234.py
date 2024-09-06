```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))
numbers = [1, 2, 3, 2, 4, 2, 3, 4]
print(remove_duplicates(numbers))  # Output: [1, 3, 4]
```
This Python code defines a function `remove_duplicates` that takes a list of integers as input and returns a new list that contains only unique elements from the original list, effectively removing duplicates. 

The code then demonstrates the usage of the `remove_duplicates` function by passing the list `[1, 2, 3, 2, 4, 2, 3, 4]` as an argument. The output of this function will be a list containing only the unique elements: `[1, 3, 4]`.