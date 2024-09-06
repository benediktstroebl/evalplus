```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [x+1 for x in l]

# Test case 1
def test1():
    assert incr_list([1, 2, 3]) == [2, 3, 4]

# Test case 2
def test2():
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test case 3
def test3():
    assert len(incr_list([99, 45, 24])) == 3
    assert incr_list([99, 45, 24]) == [100, 46, 25]

# Run all the tests
if __name__ == "__main__":
    unittest.test()

```

The code defines a function `incr_list` that takes a list l as input and returns a new list with elements incremented by 1. The test cases are then defined to verify the correctness of the `incr_list` function. The `unittest.test` module is run all all the tests to check if the function is working as expected.