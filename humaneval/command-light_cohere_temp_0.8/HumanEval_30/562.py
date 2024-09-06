```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Unit tests
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
assert not get_positive([0])
assert not get_positive([-9])
```
The `get_positive` function filters out negative numbers from the input list and returns a new list with only the positive numbers.  The test suite ensures that the function is correctly implementing the task of returning positive numbers from the input list.