```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num not in numbers[numbers.set()]]
```
# unit tests
numbers = [1, 2, 3, 2, 4, 2, 3]
assert remove_duplicates(numbers) == [1, 3, 4], "Input list contains duplicates"
assert sorted(remove_duplicates(numbers)) == [1, 2, 3, 4], "Sorted list contains duplicates"
assert len(remove_duplicates([1, 2, 3, 4, 2, 2, 3])) == 6, "Size should be 6"
assert len(remove_duplicates([1, 2, 3, 4, 5, 2, 3])) == 5, "Size should be 5"
```