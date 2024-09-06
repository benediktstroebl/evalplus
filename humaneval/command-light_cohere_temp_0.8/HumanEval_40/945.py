```python
def triples_sum_to_zero(l: list):
    if len(set(l)) != 3:
        return False
    s = 0
    for i in l:
        s += i
    return s == 0
```