```python
def triples_sum_to_zero(l: list):
    if not in [0, 3]:
        return True
    if sum(l) < 0:
        return False
    for elt in l:
        if sum([x for x in l if x != elt]) < 0:
            return False
    return True
```