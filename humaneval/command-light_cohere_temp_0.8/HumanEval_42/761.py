```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i + 1 for i in l] + [n]
    return result

# Test suite
def test_incr_list():
    tests = [
        ([1, 2, 3], [5, 3, 5, 2, 3, 3, 9, 0, 123])
    ]

    for test in tests:
        expected = [2, 3, 4]
        got = incr_list(test)
        assert expected == got, f"Test case {test} failed."

# Run the tests
test_incr_list()
 ```

The provided Python script defines a function incr_list that increments elements in a given list by 1 and adds the original list and the number of elements in the list. The test_incr_list function contains a series of test cases, each with an expected list and the result of the incr_list function applied to the test input. 

The test_incr_list function then runs the test suite using the unittest module.