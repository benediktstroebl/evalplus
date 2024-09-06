```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test cases
tests = [
    """
    def test_incr():
        return incr_list([1, 2, 3]) == [2, 3, 4]
    """
]

# Run all test cases
test_suite = unittest.TestCase('tests')

# Run the test suite and get the test results
results = unittest.result.fail(tests())

# Print the test results
print(results)
```