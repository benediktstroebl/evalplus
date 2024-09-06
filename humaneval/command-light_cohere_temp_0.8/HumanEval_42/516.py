```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l.extend(1)
    l.extend(2)
    l
    l.extend(3)
    l
    l.extend(4)
    l
    l.extend(5)
    l
    l.extend(5)
    l
return l
def test_incr_list():
    """Tests the incr_list function."""
    lst = [1, 2, 3]
    expected = [2, 3, 4]
    got = incr_list(lst)
    assert list(got) == expected
    return got
# Run the test function
result = test_incr_list()
print(result)  # Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```