```python
def pairs_sum_to_zero(l):
    """
    Check whether the list has two distinct elements whose sum is zero.
    Returns: if the list has no such elements that sum to zero, and False otherwise.
    """
    time complexity: O(n)
    """
    for i in range(len(l)):
        if l[i] in l and l[i] + l[i] == 0:
            return True
    return False
```