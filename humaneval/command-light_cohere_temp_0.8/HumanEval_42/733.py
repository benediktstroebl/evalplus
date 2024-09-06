```python
def incr_list(lst):
    """Return list with elements incremented by 1"""
    lst[:] += [1]
    return lst

#Test cases
test_incr_list = [
    ((1, []), "Should return list with elements [1, 2, 3]"),
    (([5, 3, 5],), "Should return list with elements [6, 4, 6]"),
    (([],), "Should return empty list"),
    (([1, 2, 3, 4, 5, 6],), "Should return list with elements [3, 4, 6, 7]"),
    (([2, 3, 4, 5],), "Should return list with elements [5, 6, 7]")
]

# Function test
def test_incr_list():
    for case in test_incr_list:
        assert incr_list(case[0]) == case[1], "Invalid result: " + str(case[1]) + " vs expected: " + str(case[0])

# Run the tests
test_incr_list()
```
The provided code defines a Python function `incr_list`, which returns a list with elements incremented by 1. It then provides a test cases to verify the functionality of the function, and the `test_incr_list` function runs these tests to ensure the correctness of the `incr_list` function.