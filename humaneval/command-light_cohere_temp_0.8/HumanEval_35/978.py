```python
def max_element(l: list):
    """Return maximum element in the list"""
    return max(l)

# Test cases
test_max_element = [
    lst = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
    assert max_element(lst) == 123, "Max element not found"
]

lst2 = [5, -10, 3, -5, 2]
assert max_element(lst2) == -10, "Wrong result for list2"

lst3 = [1, 2, 3, 4, 5]
assert max_element(lst3) == 5, "Wrong result for list3"

# Built-in types
assert max(range(10)) == 10, "Wrong result for range"

# Error cases
try:
    x = "hello"
    assert max_element("hello") == None, "Error: max with non-list type"
except AssertionError as e:
    print(f"Error message: {e}")
```