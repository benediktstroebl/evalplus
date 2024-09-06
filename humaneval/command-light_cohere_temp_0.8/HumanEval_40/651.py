```python
def triples_sum_to_zero(l: list):
    n = len(l)
    for i in range(n // 3):
        if sum(l[i*3:(i+1)*3]) <= 0:
            return True
    return False
```