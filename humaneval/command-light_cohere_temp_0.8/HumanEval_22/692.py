```python
from typing import List
def filter_integers(values:
    return [x for x in values if isinstance(x, int)]

# Test case 1
values1 = ['a', 3.14, 5]
result1 = filter_integers(values1)
assert isinstance(result1, list)
assert all(isinstance(x, int) for x in result1)

# Test case 2
values2 = [1, 2, 3, 'abc', {}, []]
result2 = filter_integers(values2)
assert isinstance(result2, list)
assert all(isinstance(x, int) for x in result2)

# Test case 3
values3 = List[1, 2, 3, 'abc', {}, []]
result3 = filter_integers(values3)
assert isinstance(result3, list)
assert all(isinstance(x, int) for x in result3)
``` 
The code defines a function `filter_integers` that takes a list of values as an argument and returns a new list containing only the integers from the original list. The code uses the fact type and assert statements to test the correctness of the `filter_integers` function with the provided test cases.