```python
def pairs_sum_to_zero(l):
    """
    Returns True if all elements in the list sum to zero, False otherwise.
    """
    for i in range(1, len(l)):
        s = sum(l[i:])
        if s != 0:
            return False
    return True
```