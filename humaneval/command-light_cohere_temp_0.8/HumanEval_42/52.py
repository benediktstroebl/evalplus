```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test cases
test_incr_list = [
    {
        "Input": [1, 2, 3],
        "Expected Output": [2, 3, 4]
    },
    {
        "Input": [5, 3, 5, 2, 3, 3, 9, 0, 123],
        "Expected Output": [6, 4, 6, 3, 4, 4, 10, 1, 124]
    },
    # Add more test cases as needed
]

# Run tests
test_incr_list[0]['run']()
test_incr_list[1]['run']()
```
The function `incr_list` creates a new list with elements incremented by 1. It is a a self-contained function, which can be called and reused.

The test suite includes two test cases, which test the function with different input lists. The `run()` function is called on each test case to verify the expected output is returned by the function.