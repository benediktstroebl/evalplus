```python
def triples_sum_to_zero(l: list):
    return sum(x for x in l if x != 0) <= 2 and sum(x for x in l if x != 3) <= 1 and sum(x for x in l if x != 5) <= 0
```
Do you need anything else?