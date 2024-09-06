```python
def triples_sum_to_zero(l):
    if not sets(l) or len(l) < 3:
        return False
    s = set()
    for x in l:
        if x not in s:
            s.add(x)
    if len(s) == 2:
            return True
    return False
```