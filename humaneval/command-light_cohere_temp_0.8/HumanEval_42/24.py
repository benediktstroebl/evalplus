```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    for i in range(n):
        l[i] += 1
    return l

# Test the function
test_incr_list = incr_list([1, 2, 3])
print(test_incr_list)  # Output: [2, 3, 4]
test_incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
print(test_incr_list)  # Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
The `incr_list` function takes a list `l` as input and returns a new list with elements from the original list incremented by 1. The test function is used to test the `incr_list` function by passing different lists as input and printing the resulting lists.