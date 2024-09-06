```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(1)
    return l + [0]

def test_incr_list():
    """Test incr_list function"""
    lst = [5, 3, 5, 2, 3, 3, 9, 0, 123]
    expected = [6, 4, 6, 3, 4, 4, 10, 1, 124]
    for el, exp in zip(lst, expected):
        assert el == exp, f"List elements don't match: {el} != {exp}"
    return "Test passed"

# Call the function and run the test
incr_list(lst)
test_incr_list()
```