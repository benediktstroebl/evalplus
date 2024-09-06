```python
from typing import List
def filter_integers(values):
    return [x for x in values if type(x) == int]

# Test case 1
values1 = ['a', 3.14, 5]
result1 = filter_integers(values1)
assert result1 == [5]

# Test case 2
values2 = [1, 2, 3, 'abc', {}, []]
result2 = filter_integers(values2)
assert result2 == [1, 2, 3]

# Test case 3
values3 = [1, 2, 3, 4, 'five', 6]
result3 = filter_integers(values3)
assert result3 == [1, 2, 3, 4]
```
The code defines a function `filter_integers` that takes a list of values as input and returns a new list containing only the integer elements from the input list. It employs a filtering logic using the `if` condition to identify integer elements in the list. The provided test cases demonstrate the expected behavior of the function.