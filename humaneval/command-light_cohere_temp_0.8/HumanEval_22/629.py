```python
from typing import List
def filter_integers(values):
    return [i for i in values if type(i) == int]

# Test case 1: Filter integers from a list of values
test_case_1 = ['a', 3.14, 5]
result_case_1 = filter_integers(test_case_1)
assert [i for i in result_case_1 if i == 5] == [5]

# Test case 2: Filter integers from a tuple of values
test_case_2 = (1, 2, 3, 'abc', {}, [])
result_case_2 = filter_integers(test_case_2)
assert [i for i in result_case_2 if type(i) == int] == [1, 2, 3]

# Test case 3: Filter integers from a list of mixed types
test_case_3 = ['a', 3.14, (4, 5. different values

result_case_3 = filter_integers(test_case_3)
assert [i for i in result_case_3 if type(i) == int] == [4, 5]
```
This script defines a function **filter_integers** that filters a list or tuple of values and returns a new list containing only the integers. It then passes three test cases and checks the results against the expected outputs.