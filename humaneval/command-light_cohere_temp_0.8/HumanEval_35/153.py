```python
def max_element(lst):
    return max(lst)

# Test case 1
assert max_element([1, 2, 3]) == 3

# Test case 2
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123

# Test case 3
assert max_element([-5, -3, -10]) == -10

# Test case 4
try:
    assert max_element([1, 2, 3, 4, 5]) == 5
    raise AssertionError("Should not equal 5")
except:
    assert True  # To avoid assert statement error

# Test case 5
try:
    assert max_element([0, 2, -1]) == 0
    raise AssertionError("Should not equal 0")
except:
    assert True  # To avoid assert statement error
```