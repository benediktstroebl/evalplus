```python
from typing import List
def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test case 1
values1 = [3.14, 'a', 5]
result1 = filter_integers(values1)
assert len(result1) == 3

# Test case 2
values2 = [1, 2, 3, 'abc', {}, []]
result2 = filter_integers(values2)
assert len(result2) == 3

# Test case 3
values3 = [1, 2, 3, 4, 5, 'abc']
result3 = filter_integers(values3)
assert len(result3) == 4

# Test case 4
# Error: TypeError: 'filter() missing 1 required positional argument'
# VALUES in filter_integers([1, 2, 3, 'abc', {}])
``` 
The provided Python script defines a function `filter_integers` that filters a list of values to extract only integers. This function utilizes the core Python list comprehension to accomplish this task. The test cases that follow, each passing different sets of values and verifying the output against the expected length of integers.