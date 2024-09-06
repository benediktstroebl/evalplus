```python
def triples_sum_to_zero(lst):
    # Write your code here
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

The function examines all possible triples of elements in the list `lst`. It uses a set called `seen` to keep track of any triples it has previously seen in order to avoid duplicates. The function returns `True` if any distinct triple has a sum of zero and `False` otherwise.