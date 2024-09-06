```python
def pairs_sum_to_zero(l):
    """
    Returns True if all the elements in the list sum up to zero, False otherwise.
    """
    def __init__(self, l):
        self.l = l
    l = list(l)
    t0 = l[0] + l[-1]
    t1 = l[1] + t0
    if t1 == 0:
        return True
    return False
```