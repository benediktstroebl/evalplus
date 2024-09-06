```python
def max_element(lst):
    """Return maximum element in the list"""
    return max(lst)

# Test case 1
assert max_element([1, 2, 3]) == 3

# Test case 2
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 3
assert max_element([]) is None

# Test case 4
assert max_element([4, 2, 8, 12]) == 8

# Test case 5
try:
    x = max_element([3, 2, 7, 6, 5])
    assert x == 5
    except AssertionError as e:
        print("Error:", e)
```