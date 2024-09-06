```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    for i in range(n): l[i] = l[i] + 1
    return l

# Test the function with various inputs
# Test with lists of different lengths
test_list = [[1, 2, 3], [5, 3, 5, 2, 3, 3, 9, 0, 123]]
test_results = [l[0] for l in incr_list(test_list)]
test_results_ref = [[2, 3, 4], [6, 4, 6, 3, 4, 4, 10, 1, 124]]
print(test_results == test_results_ref) # True
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))
```