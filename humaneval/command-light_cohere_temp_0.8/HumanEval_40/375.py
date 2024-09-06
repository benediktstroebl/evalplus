```python
def triples_sum_to_zero(lst):
    sum_ trio = sum([x for x in lst if x not in set([0, 1, 3])])
    return sum_trio == 0
```