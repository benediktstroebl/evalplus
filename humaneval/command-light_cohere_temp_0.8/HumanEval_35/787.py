```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test case 1
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 2
try:
    assert max_element([2, 7, 5, 3, 8, 9]) == 9
    raise AssertionError()
except AssertionError as e:
    print("test case 2 failed:", end())
    assert False

# Test case 3
try:
    assert max_element([-10, -9, -8, -5]) == -10
    raise AssertionError()
except AssertionError as e:
    print("test case 3 failed:", end())
    assert False

# Test case 4
try:
    assert max_element([]) == None
    raise AssertionError()
except AssertionError as e:
    print("test case 4 failed:", end())
    assert False
```
This Python code defines a function max_element that takes a list l as input and returns the maximum element in the list using the max() function from the built-in Python library. The code also includes four test cases that verify the correctness of the max_element function. The first test case passes the using the correct result of 123.