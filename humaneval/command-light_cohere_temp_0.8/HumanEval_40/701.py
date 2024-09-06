```python
def triples_sum_to_zero(l: list):
    return sum([x for x in l if x not in set([0, x for y in l if y != x])]) <= 0
```
Do you have any other questions about Python programming?