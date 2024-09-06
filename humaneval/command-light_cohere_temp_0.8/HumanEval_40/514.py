```python
def triples_sum_to_zero(l: list):
    n = len(l)
    if n < 3:
        return False
    sum = 0
    for i in range(0, n, 2):
        sum += l[i] + l[i+1]
    return sum <= 0
```