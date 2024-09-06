```python
def triples_sum_to_zero(l: list):
    """
    Returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    seen = set()
    for a in l:
        if a < 0:
            continue
        for b in l:
            if b < 0 or b == a:
                continue
            for c in l:
                if c < 0 or c == a or c == b:
                    continue
                if a + b + c == 0 and a not in seen and b not in seen and c not in seen:
                    return True
                seen.add(a)
                seen.add(b)
                seen.add(c)
    return False
```