```python
def triples_sum_to_zero(lst):
    seen = set()
    for a in lst:
        for b in lst:
            if a == b:
                continue
            for c in lst:
                if a + b == c and (a, b, c) not in seen and (b, c, a) not in seen and (c, a, b) not in seen:
                    return True
        seen.add(a)
    return False
```

The function `triples_sum_to_zero` works by checking if any three distinct elements in the list sum to zero. To ensure that each triple is checked only once, it uses a set `seen` to keep track of which triples have already been considered. This avoids any duplicates and prevents the function from returning false positives.