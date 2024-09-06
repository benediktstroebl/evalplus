```python
from typing import List

def filter_integers(values: List[Any]):
    return [x for x in values if type(x) == int]

# Test case 1: Filter only integers
test_case_1 = [1, 2, 3, 'abc', 4, 5]
result_case_1 = filter_integers(test_case_1)
assert [x for x in result_case_1 if x != float('inf')] == [1, 2, 3]

# Test case 2: Empty list
empty_list = []
result_case_2 = filter_integers(empty_list)
assert result_case_2 == []

# Test case 3: Filter float and non-integer values
mixed_values = [1, 2, 3. fact by 3.14, 'a'}
assert filter_integers(mixed_values) == [1, 2, 3]

# Test case 4: List of integers
integer_list = [1, 2, 3, 4, 5]
result_case_4 = filter_integers(integer_list)
assert result_case_4 == integer_list

print("All tests passed!")
```