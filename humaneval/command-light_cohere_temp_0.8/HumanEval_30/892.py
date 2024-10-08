```python
def get_positive(lst):
    return [num for num in lst if num >= 0]

# Test the function with different input lists
assert get_positive([-1, 2, -4, 5, 6]) == [2, 5, 6]
assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123]
assert not get_positive([5, 3, -5, 2, -3, 3, 9, 0, -1])

```
The function get_positive takes a list as an argument and returns a new list containing only the positive numbers from the input list. The test cases in the script verify that the output of the get_positive function matches the expected results.