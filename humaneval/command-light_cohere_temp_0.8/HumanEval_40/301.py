```python
def triples_sum_to_zero(l: list):
    n = len(l)
    for i in range(n // 3):
        cur_sum = 0
        for j in range(i * 3 + 1, n):
            cur_sum += l[j]
        if cur_sum <= 0:
            return True
    return False
```