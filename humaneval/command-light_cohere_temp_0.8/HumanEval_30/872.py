```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test cases
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
assert not get_positive([5, 3, -5, -20, 2, -3, 3, 9, 0, 123])
assert not get_positive([ Double(-12), 2.64, True, -99.

```
This code defines a function, `get_positive`, which takes a list as input and returns a new list containing only the positive elements from the input list. The test cases verify that function's behavior for different input scenarios.