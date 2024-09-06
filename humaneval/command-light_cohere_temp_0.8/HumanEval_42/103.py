```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [i+1 for i in l]

# Test case 1
def test_incr_list():
    assert incr_list([1, 2, 3]) == [2, 3, 4]

# Test case 2
def test_incr_list2():
    assert incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test case 3 (with failure)
def test_incr_list3():
    assert incr_list([10, 2, 3]) == [10, 3] 

if __name__ == "__main__":
    # Run all test cases
    test_incr_list()
    test_incr_list2()
    test_incr_list3()
```
This Python script defines the `incr_list` function that returns a list with elements incremented by 1. It also includes three test cases: `test_incr_list`, which passes, and `test_incr_list2` that fails. Finally, the script runs all test cases to verify the correctness of the `incr_list` function.