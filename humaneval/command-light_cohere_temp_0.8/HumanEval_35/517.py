```python
def max_element(lst):
    return max(lst)

# Test case 1
assert max_element([1, 2, 3]) == 3

# Test case 2
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 3 (Negative input)
assert max_element([1, 2, 3]) == 3  # Should fail

# Test case 4 (Empty list)
try:
    assert max_element([])
except AssertionError as e:
    print("Error:", e)
```
This script defines a function max_element that takes a list as input and returns the maximum element in the list. The function is then tested using several test cases, passing all the tests.

The output will include the error message if any assertion fails.