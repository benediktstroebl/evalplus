```python
from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in set(numbers) if num not in numbers]

# Unit tests
numbers_list = [1, 2, 3, 2, 4, 3, 1, 4]
result = remove_duplicates(numbers_list)
assert result == [1, 3, 4]

```
This function called `remove_duplicates` takes a list of integers as input and returns a new list with all distinct integers from the original. It uses the value of the set of all elements in the original list and then uses the membership test for elements that are not in the set to filter out duplicates and keep only the distinct elements.