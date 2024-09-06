```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    new_list = [x + 1 for x in l]
    return new_list

# Test suite
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert not incr_list([]) == []
    assert not incr_list([5, 6, 7]) == [5, 6, 7]

# Main function to call test suite and execute function
def main():
    test_incr_list()
    incr_list([1, 2, 3])

# This code serves as an example of self-contained Python script with a function to increment elements in a list and pass tests for correct function behavior
```