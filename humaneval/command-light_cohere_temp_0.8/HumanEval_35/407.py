```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test case 1
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 2
try:
    x = max_element([-83, -82, -80, -75])
    assert x == -75
    except AssertionError as ae:
        print(f"Error: {ae} in test case 2")

# Test case 3
try:
    x = max_element([])
    assert x == None
    print("Test case 3 passed")

# Test case 4
try:
    x = max_element([1, 2, 3])
    assert x == 3
    print("Test case 4 passed")

```
This code defines a function max_element that takes a list as input and returns the maximum element in the list. It uses the `max()` function to get the maximum value of the list. The test cases ensure that the function is working correctly and print appropriate error messages if any test fails.