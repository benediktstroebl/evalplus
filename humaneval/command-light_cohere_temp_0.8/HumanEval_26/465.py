```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    seen = set()
    result = [x for x in numbers if x not in seen and x not in numbers[:-len(seen)]]
    return result

# Test case:
numbers = [1, 2, 3, 2, 4]
print(remove_duplicates(numbers))
```
This Python function, `remove_duplicates`, takes a list of integers as input and returns a new list containing only the unique integers. The function uses a set to keep track of the elements that have already been encountered. The `result` list is populated with elements that are not in the `seen` set and are not duplicates.

This function can efficiently solve the problem of removing duplicate elements from a list of integers.

Feel free to ask any further questions!