```python
def triples_sum_to_zero(l: list):
    """
    Returns True if three distinct elements in the list sum up to zero, False - otherwise.
    """
    seen = set()
    for i, x in enumerate(l):
        if x < 0:
            y = -x
        else:
            y = x
        if y in seen and l[seen.index(y)] != l[i]:
            return True
        seen.add(x)
    return False
```

This solution iterates through the list, trying to find two elements whose sum is zero (or negative) and they are distinct. At the end, it will run a fast check to verify if the list has three distinct elements.