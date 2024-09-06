```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i+1 for i in l] + l
    return result

# Test the function with known good inputs/outputs
test_incr_list = []
test_incr_list.push([1, 2, 3])
test_incr_list.push([5, [5, 3, 5, 2, 3, 3, 9, 0, 123])

for test in test_incr_list:
    assert list(incr_list(test)) == test, f"Failed with [{test}]")
```
The code defines a function incr_list that returns a list with elements incremented by 1. It also includes a list of tests, and for each test the function is invoked with the test list, and the result is compared with the expected output. If the result does not match, the test fails and an error message is printed.