```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [x + 1 for x in l]
    return result

# Test cases
test_incr_list = [
    [(1, [1, 2, 3])],
    [(2, [5, 3, 5, 2, 3])],
    [(3, [0, 2, 3])],
    [(4, []),
    [(5, [9, 0, 123])]
]

def test_func(test_case):
    l = test_case[0]
    expected = test_case[1]
    got = incr_list(l)
    assert expected == got, f"Error in test case: {test_case}"

# Run the tests
test_incr_list = cast(test_incr_list, str)
sc = unittest.result_writer()
print(test_incr_list)
sc.
```
Now the above code defines a function that takes a list and returns a new list with elements incremented by 1. The test cases provide different lists for which the function is invoked, and the expected results are compared against the actual results using `assert`.  Finally, the `unittest` module is used to run the tests.