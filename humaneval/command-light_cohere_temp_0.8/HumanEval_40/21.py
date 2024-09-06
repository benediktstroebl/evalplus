```python
def triples_sum_to_zero(l: list):
    if not set(map(sum, l)) & {0} and len(l) > 2:
        return True
    return False
```