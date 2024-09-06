```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    n = len(l)
    result = [i + 1 for i in l]
    assert len(result) == n, f"Length of result list should be {n}, but is {len(result)}."
    assert all(map(lambda x: x == i+1 for i, l)), f"Elements of original list should be {l}, but are {l}."
    return result

# Example usage:
l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result_new = incr_list(l)
assert l == result_new, "Original list should be equal to the incremented list."
```
This script defines a function `incr_list` that takes a list `l` as input and returns a new list with elements incremented by 1. The function includes assert statements to validate the correctness of the returned list, and the equality between the original list and the incremented list. The example usage demonstrates how to use the function with a sample input list `l`.