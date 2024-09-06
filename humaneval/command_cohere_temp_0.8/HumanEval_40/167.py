```python
def triples_sum_to_zero(lst):
    seen = set()
    for a in lst:
        for b in lst:
            if a == b:
                continue
            for c in lst:
                if c == a or c == b:
                    continue
                if (a + b + c) == 0 and (a, b, c) not in seen:
                    seen.add((a, b, c))
                    return True
    return False
```

The function examines all possible triples of elements in the list, and checks if the sum of the three elements is zero. If so, it returns True if it has not been checked before otherwise, it returns False.