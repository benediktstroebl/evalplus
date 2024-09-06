```python
from typing import List
def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test case 1
values1 = [1, 2, 3, 'abc', 5]
test_values1 = filter_integers(values1)
assert set(test_values1) == set([1, 2, 3])

# Test case 2
values2 = [1, 2, 3, 'abc', {}]
test_values2 = filter_integers(values2)
assert set(test_values2) == set([1, 2, 3])

# Test case 3
values3 = [3.14, 'hello']
test_values3 = filter_integers(values3)
assert set(test_values3) == set([3])
```
The function `filter_integers` takes a list of values as an argument and returns a new list that contains only the integers from the input list. It uses a Python list comprehension to filter out the integers from the input list.