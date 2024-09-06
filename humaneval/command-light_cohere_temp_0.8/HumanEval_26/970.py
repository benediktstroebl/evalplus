```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [n for n in numbers if n not in set(numbers)]
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))  # Expected Output: [1, 3, 4]
```
This Python function called `remove_duplicates` takes a list of integers as an argument and returns a new list with duplicate elements removed. It uses the unique elements in the set function to create a new set of integers, then iterates through the original list and adds elements that are not in the set, effectively removing duplicates.