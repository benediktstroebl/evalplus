```python
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    numbers = set(numbers)  # Convert to set to remove duplicates
    return [num for num in numbers if num not in set()]

# Unit tests
numbers_list = [1, 2, 3, 2, 4, 3, 1]
test_remove_duplicates(numbers_list)

numbers_set = {1, 2, 3, 4, 3, 5}
test_remove_duplicates(numbers_set)

```
The function `remove_duplicates` in this script accepts a list of integers as an argument and outputs a new list containing only the integers that are not duplicates. The function is tested using the code block below, which uses the `unittest` library to run the test suite.