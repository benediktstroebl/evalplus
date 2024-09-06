```python
def triples_sum_to_zero(lst):
    sum_ trio = sum((x, y, z) for x, y, z in zip(*lst)))
    return sum_trio <= 0
```