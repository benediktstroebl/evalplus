```python
def pairs_sum_to_zero(l):
    """
    checks whether a list of integers has two sumzero elements
    Returns: bool
    """
    if len(l) < 2: return False
    s = 0
    for x in l:
        s += x
    if s % 2 != 0: return False
    return True
```