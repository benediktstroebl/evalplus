```python
from typing import List
def remove_duplicates(numbers: List[int]) -> List[int]:
    return [n for n in numbers if n not in set(numbers)]

# Unit tests
numbers_list = [1, 2, 3, 2, 4, 3, 1]
result = remove_duplicates(numbers_list)
should_be = [1, 2, 3, 4]
assert result == should_be, "Expected: {} Got: {}".format(result)

numbers_set = {1, 2, 3, 4}
result = remove_duplicates([3, 4, 1, 2])
should_be = []
assert result == should_be, "Expected: {} Got: {}".format(result)

```
The function remove_duplicates in this script accepts a list of integers and outputs a fresh list with any duplicates eliminated. The unit tests section runs a script with a variety of test cases to make sure the function is operating properly.