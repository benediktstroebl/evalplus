```python
from typing import List

def filter_integers(values:
    """

    filtered_numbers = [num for num in values if isinstance(num, int)]
    return filtered_numbers

# Test cases
test_data = [['a', 3.14, 5], [1, 2, 'abc', {}, []]

test_case_1 = test_data[0]
test_case_2 = test_data[1]
test_case_3 = test_data[2]

result_1 = filter_integers(test_case_1)
result_2 = filter_integers(test_case_2)
result_3 = filter_integers(test_case_3)

assert len(result_1) == 1
assert result_1[0] == 5

assert len(result_2) == 3
assert result_2[0] == 1 and result_2[1] == 2 and result_2[2] == 3

assert len(result_3) == 0

print("All tests passed!")
```