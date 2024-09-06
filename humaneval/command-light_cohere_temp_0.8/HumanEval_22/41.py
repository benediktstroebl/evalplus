```python
def filter_integers(values):
    return [num for num in values if isinstance(num, int)]

# Test case 1
values1 = ['a', 3.14, 5]
result1 = filter_integers(values1)
assert len(result1) == 3

# Test case 2
values2 = [1, 2, 3, 'abc', {}, []]
result2 = filter_integers(values2)
assert len(result2) == 3

# Test case 3
values3 = [1, 2, 3, [], 0]
result3 = filter_integers(values3)
assert len(result3) == 3

# Test case 4
values4 = [1, 2, 'abc]
result4 = filter_integers(values4)
assert len(result4) == 0
```
This script defines a function **filter_integers** that filters a given list of values and returns a new list containing only the integers. It then passes four test cases to this function and validates the results against the expected behavior.