```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)
    return [num for num in numbers if num not in numbers]

numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # expected output: [1, 3, 4]
```
This script defines a function **remove_duplicates** that takes a list of integers as input and returns a new list with elements that are not duplicates. The set function is used to remove duplicates, and then a list comprehension is used to filter out the unique elements from the original list.