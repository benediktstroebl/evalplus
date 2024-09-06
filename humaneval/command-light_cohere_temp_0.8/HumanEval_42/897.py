```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    return [x + 1 for x in l]

# Test cases
test_incr_list = [
    [
        ("List with integers", incr_list([1, 2, 3]) == [2, 3, 4]),
        ("List with strings", incr_list(["a", "b", "c"]) == ["b", "c", "d"])
    ]

def test_case_success(test_suites):
    """Check if test cases pass."""
    for case, (want, actual) in test_suites.
        print(f"{case}: Expected: {want}, Actual: {actual}")
        assert want == actual, f"{case} failed."
    test_incr_list

test_incr_list()
```
This code defines a function incr_list that takes a list l as input and returns a new list with elements incremented by 1. The test_incr_list function contains a list of test cases, where each test case consists of a description and the expected output of the incr_list function applied to a specific list. The test_case_success function checks if each test case passes, by comparing the actual output of incr_list with the expected output. It uses the test.on the test_suites, which are lists of tuples, each containing a test description and the expected output of the incr_list function.