```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(l[-1] + 1)
    return l

# Test cases
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert len(incr_list([10, 20, 30]))) == 3
    assert incr_list([10, 20, 30, 40]) == [20, 30, 40]

# Main execution
test_incr_list()
```