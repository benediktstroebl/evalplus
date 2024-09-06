```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [n for n in set(numbers) if n not in numbers]

# Unit tests
numbers_list = [1, 2, 3, 2, 4, 3, 5]
test_result = remove_duplicates(numbers_list)
assert len(test_result) == 4, "Unit test failed: Length should be 4, but is {}"
assert set(test_result) == {1, 3, 4}
```