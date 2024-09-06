```python
def incr_list(lst):
    lst[::] = lst[-1] + 1
    return lst

# Test
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]

# Test (negative increment)
def test_negative_incr_list():
    assert incr_list([5, 3, 5], -1) == [5, 3, 5]

# Test (empty list)
def test_empty_list():
    assert incr_list([]) == []
```
The code defines a function `incr_list` that increments the last element of a list by 1 and returns the modified list. It includes a test functions to test the `incr_list` function with various inputs, including empty lists and lists with specific elements.