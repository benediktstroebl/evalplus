```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test cases
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
assert not get_positive([5, 3, -5, -20, 2, -3])
assert not get_positive([10, 9, -9, -100])
```
This script defines a function that takes a list and returns a new list with only the positive elements from the input. It then provides some test cases to validate the functionality. The test cases cover a expected results for various input scenarios.