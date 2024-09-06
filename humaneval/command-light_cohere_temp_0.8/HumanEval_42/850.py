```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    l.append(1)
    return l + [1]

# Test function
def test_incr_list():
    """Return list with elements decremented by 1."""
    l = [1, 2, 3]
    l.append(1)
    return l - [0, -1, -2]

# Test cases
tests = {
    "Original list": [1, 2, 3],
    "Increment": [2, 3, 4],
    "Decrement": [-1, -2, -3],
    "Combined increment and decrement": [4, 3, 2],
}

# Run tests
for test in tests. print result = test_incr_list()
for test, want in tests. result
print(f"Test: {test}\nWant: {want}\nResult: {result}")
```

This script defines a function **`incr_list`** that increments each element in a list by 1, and a test function **`test_incr_list`** that returns a list with elements decremented by 1. The test cases include original list, increment operation, and decrement operation tests. The script then runs the results of each test case are printed.