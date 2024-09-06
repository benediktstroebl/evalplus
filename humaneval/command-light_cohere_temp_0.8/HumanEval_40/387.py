```python
def triples_sum_to_zero(lst):
    return any(sum(x) == 0 for x in lst) and sum(x for x in lst) <= 3
```