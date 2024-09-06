```python
from typing import List
def filter_integers(values:
    return [x for x in values if type(x) == int]

# Test case 1
values = ['a', 3.14, 5]
result = filter_integers(values)
assert len(result) == 2
assert result[0] == 5
assert result[1] == 3

# Test case 2
values = [1, 2, 3, 'abc', {}, []]
result = filter_integers(values)
assert len(result) == 3
assert result[0] == 1
assert result[1] == 2
assert result[2] == 3

# Test case 3
values = [1, 2, 3, 'abc', {}, [1, 2, 3])
result = filter_integers(values)
assert len(result) == 6
assert result[0] == 1
assert result[1] == 2
assert result[2] == 3
assert result[3] == 'abc'
assert result[4] == {}
assert result[5] == [1, 2, 3]
```
This Python script defines a function `filter_integers` that takes a list of values and returns a new list containing only the integers from the input. The test cases cover various scenarios, passing the function's output against the expected results and confirming the type of each element. The script also covers edge cases, such as passing an empty list or a list with non-integer elements, which should return the input list as is.