```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

def test_incr_list():
    """Function to test the incr_list function."""
    assert incr_list([1, 2, 3]) == [2, 3, 4]
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]
    assert not incr_list([])
    assert not incr_list([1, 2, 3, 4, 5])

if __name__ == "__main__":
    test_incr_list()
```

This Python script presents a self-contained function, `incr_list`, designed to produce a new list with list elements incremented by 1. It additionally includes a test_incr_list, a function to assess the correctness of the `incr_list` function. The function employs assertions to ensure the expected output aligns with the specified behavior of the `incr_list` function. Finally, the `__name__ == "__main__"` construct is employed to execute the `test_incr_list` function when the script is run, thereby enabling the test suite to function properly.