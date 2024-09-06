```python
def pairs_sum_to_zero(l):
    """
    Checks if the list has two elements whose sum is less than or equal to zero.
    Returns True if the

    """
    s = set(sum(a) for a in l)
    if len(s) != 1:
        return False
    for a in s:
        if a <= 0:
            return False
    return True
```