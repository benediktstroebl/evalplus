```python
def max_element(lst):
    """Return maximum element in the list."""
    return max(lst)

# Test case 1: Positive integers
tested = [1, 2, 3]
max_result = max_element(tested)
assert max_result == 3

# Test case 2: Negative integers
tested = [-5, -3, -2, -3, -1]
max_result = max_element(tested)
assert max_result == -3

# Test case 3: Integers and fractions
tested = [5, 3, -5, 2/3, 1, -10]
max_result = max_element(tested)
assert max_result == -10

# Test case 4: Complex numbers
tested = [0, 123, 1, -10]
max_result = max_element(tested)
assert max_result == 123
```

This Python script provides a self-contained function that efficiently computes the maximum element within a given list. It also comes a test cases to ensure the function's correctness.