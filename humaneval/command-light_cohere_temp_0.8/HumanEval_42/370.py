```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    l.append(l[-1] + 1)
    return l

# Test the function with various inputs
tests = [ [1, 2, 3], [5, 3, 5, 2, 3, 3, 9, 0, 123], [(), []] ]

for i, test in enumerate(tests):
    result = incr_list(test)
    assert result == tests[i+1]  # Check if the result matches the expected output
```  This code defines a function `incr_list` that takes a list `l` as an argument and returns a new list with elements incremented by 1. The test suite uses a list of test cases, each containing a list of elements, and the code checks if the output of the `incr_list` function matches the expected output for each test case.