```python
def triples_sum_to_zero(lst):
    return all(sum(x) <= 0 for x in lst) and len(lst) == 3
```