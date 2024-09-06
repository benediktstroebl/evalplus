```python
def triples_sum_to_zero(l: list):
    """
    Returns True if three distinct elements in the list sum up to zero, False - otherwise.
    """
    seen = set()
    for i in l:
        if 0 == i:
            continue
        x, y = 0, 0
        for j in l:
            if j == i or j in seen:
                continue
            x += j
            y += x
            if y == 0:
                return True
            seen.add(x)
    return False
```

The function employs a greedy algorithm to search for two numbers `x` and `y` in the list such that `x + y + z = 0`. It initializes two variables to zero and then loops through the list. It tries to find a pair of numbers that add up to the current value of `x`. If it finds such a pair `y`, it updates `x` to this new value and resets `y` to zero. It returns `True` if it successfully finds a triplet that sums up to zero and `False` otherwise. To avoid falling into the situation where a triplet is found but no tuple of size 2 is found, the algorithm skips over zeroes and duplicates.