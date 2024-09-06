```python
def triples_sum_to_zero(l: list):
    n = len(l)
    if n < 3: return False
    sum_to_zero = sum(l)
    for i in range(n):
        if sum_to_zero < 0 and l[i] > 0: sum_to_zero += l[i]
        elif sum_to_zero < 0 and l[i] < 0: sum_to_zero -= l[i]
    return sum_to_zero == 0
```