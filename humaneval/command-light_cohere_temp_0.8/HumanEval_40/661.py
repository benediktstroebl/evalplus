```python
def triples_sum_to_zero(l: list):
    return sum(x for x in l if len({x, x + 1, x - 1}) == 2) == 0
```
Do you need help with anything else?