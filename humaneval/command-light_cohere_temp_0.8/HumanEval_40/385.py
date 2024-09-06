```python
def triples_sum_to_zero(l: list):
    if len(l) < 3: return False
    if not any(sum(x) <= 0 for x in l)): return True
    return False
```