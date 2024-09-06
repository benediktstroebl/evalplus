```python
def triples_sum_to_zero(l: list):
    return sum(x for x in l if set(x) <= 2) <= 0
```
Do you need anything else?