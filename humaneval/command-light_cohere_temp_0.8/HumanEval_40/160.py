```python
def triples_sum_to_zero(l: list):
    n = len(l)
    if n < 3:
        return False
    sum = 0
    for i in range(n):
        if l[i] > 0:
            sum += l[i]
    return sum == 0
```