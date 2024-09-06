```python
def triples_sum_to_zero(l: list):
    if len(l) < 3: return False
    sum = 0
    for el in l: sum += el
    return sum <= 0
```