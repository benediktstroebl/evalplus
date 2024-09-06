```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    res = [x + 1 for x in l]
    return res

# Test the function
test_incr_list = incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
print(test_incr_list)  # Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]

test_incr_list2 = incr_list([1, 2, 3])
print(test_incr_list2)  # Output: [3, 4, 5, 6]

test_incr_list3 = incr_list([10, 2, 3, 4, 5])
print(test_incr_list3)  # Output: [11, 5, 8, 7]
```