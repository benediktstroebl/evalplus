```python
def triples_sum_to_zero(l: list):
    # Write your code here.
    seen = set()
    for a, b in itertools.combinations(l, 2):
        if a + b == 0 and (a, b) not in seen:
            seen.add((a, b))
            if len(seen) == 3:
                return True
    return False
```

This code uses `itertools.combinations` to efficiently generate pairs of elements from the input list `l`. It uses a set called `seen` to keep track of already-seen pairs that sum to zero, to ensure that the function returns True only when three distinct pairs are found.