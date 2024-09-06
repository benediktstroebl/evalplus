```python
def triples_sum_to_zero(l):
    if not in l or len(l) < 3:
        return False
    if set(sum(x) for x in l) == {0} or set(sum(x) for x in l) == {2, 4}:
        return True
    return False
```