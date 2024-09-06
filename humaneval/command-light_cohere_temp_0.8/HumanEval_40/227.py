```python
def triples_sum_to_zero(lst):
    return any(sum(x) <= 0 for x in lst) and any(x != y for x, y in zip(lst)) == True
```