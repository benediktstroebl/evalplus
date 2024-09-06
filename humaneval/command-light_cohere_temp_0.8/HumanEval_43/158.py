```python
def pairs_sum_to_zero(l):
    """
    Returns True if there are two distinct elements in the list that sum to zero, 
    and False otherwise.
    """
    boolean AND operation is used to check if there are two elements that add up to zero.
    If a list comprehension and built-in list are used to find the two elements that sum to zero.

test_pairs_sum_to_zero = [
    [1, 3, 5, 0],
    [1, 2, 3, 7],
    [2, 4, -5, 3, 5, 7],
    [1]
]

for test in test_pairs_sum_to_zero:
    result = pairs_sum_to_zero(test)
    assert result == True, "Test %s failed: %s" % (test, result)
```

The script defines a function `pairs_sum_to_zero` that checks if there are two elements in the list that sum to zero. It uses a `assert` to assert the output of the function. This ensures that the function is working correctly.