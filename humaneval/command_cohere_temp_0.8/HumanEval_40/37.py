```python
def triples_sum_to_zero(lst):
    # Write your code here. Read the markdown for more details
    seen = set()
    for a in lst:
        for b in lst:
            if a != b and sum([a, b, c]) == 0 and (a, b, c) not in seen:
                c = -a-b
                seen.add((a, b, c))
                if len(seen) == 3:
                    return True
    return False
```

The algorithm works by traversing the list and attempting to find two elements a and b that sum up to zero. Once such a pair is found, the algorithm searches for a third element c which completes the trio (a, b, c) where `a + b + c = 0`. The brute-force nature of this approach is not the most efficient, a more sophisticated approach could be needed for very large lists. Would you like to improve on this further?