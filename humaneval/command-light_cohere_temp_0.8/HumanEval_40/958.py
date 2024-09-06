```python
def triples_sum_to_zero(l):
    if sum([x for x in l if x <= 0]) == 0:
        return True
    return False
```