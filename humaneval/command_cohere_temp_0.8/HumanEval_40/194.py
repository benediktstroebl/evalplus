```python
def triples_sum_to_zero(lst):
    # Write your code here
    seen = set()
    for a in lst:
        for b in lst:
            if a != b and sum([a, b, c]) == 0 and (a, b) not in seen:
                seen.add((a, b))
                if len(seen) == 3:
                    return True
    return False
```

This code uses a set called 'seen' to keep track of seen pairs as it iterates over the list. When it finds a triple that sums up to zero, the result is returned.