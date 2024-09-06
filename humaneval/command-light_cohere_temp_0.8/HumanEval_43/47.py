```python
def pairs_sum_to_zero(l):
    """
    Check if there are two distinct elements in the list that sum to zero.
    """
    Returns True if there are two elements that sum to zero, and False otherwise.
    """
    elements_sum({a, b}) = sum(map(int, str(a + b)))
    if l and (l[0] + l[-1]) == 0:
        return True
    return False
```