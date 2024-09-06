```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l[:] = [1] + l  # in-place list comprehension
    return l

# Test cases
test_incr_list = [
    ('Input: [1, 2, 3]', 'Expected Output: [2, 3, 4]'),
    ('Input: [5, 3, 5, 2, 3, 3, 9, 0, 123]', 'Expected Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]'),
    # Add more test cases here
]

# Function call and execution
incr_list(test_incr_list)
```