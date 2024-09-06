```python
def get_positive(l: list):
    return [num for num in l if num >= 0]

# Test cases
tests = {
    "test_get_positive": [
        """Return positive numbers in the list [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]"""
        assert get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == [5, 3, 2, 3, 9, 123, 1]
    ]
}

# Run the function and tests
score = run_tests(tests)
print("Test score:", score)
```

I hope that this Python script provides a self-contained function that solves the problem of returning only positive numbers from a list. It also includes a test cases to check the correctness of the `get_positive` function. The `run_tests` function is then used to execute both the function and tests.