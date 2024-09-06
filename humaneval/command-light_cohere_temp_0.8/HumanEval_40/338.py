```python
def triples_sum_to_zero(l):
    if sum(set(map(int, l)))) % 3 == 0:
        return True
    else:
        return False
```