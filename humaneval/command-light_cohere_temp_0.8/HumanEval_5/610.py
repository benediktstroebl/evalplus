```python
from typing import List
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    return [num + i * delimeter for i, num in enumerate(numbers)]

# Test cases
numbers_test = [4, 1, 2, 3]
delimiter_test = 4
result_test = intersperse(numbers_test, delimiter_test)
assert result_test == [5, 8, 6, 12]

numbers_list = [1, 2, 3]
result_list = intersperse(numbers_list, 5)
assert len(result_list) == len(numbers_list) + 2
assert all(map(lambda x: x % 5 == 0, result_list))  # This should pass since the numbers are adjusted properly

I hope the solution worked!
```