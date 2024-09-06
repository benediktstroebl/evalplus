```python
def triples_sum_to_zero(l: list):
    if len(set(l)) != 3:
        return False
    return sum(x) == 0
```