```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test cases for get_positive function
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
assert not get_positive([5, 3, -5, 2, -3, -4, 3]) == []
assert not get_positive([1, 2, 3, -1]) == []
```
This code defines a function `get_positive` that returns a list of positive numbers from the input list `lst`. The test cases ensure that the function is working as expected with various inputs.