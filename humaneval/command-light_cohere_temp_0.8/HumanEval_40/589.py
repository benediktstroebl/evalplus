```python
def triples_sum_to_zero(lst):
    n = len(lst)
    if n < 3:
        return False
    sum = 0
    for i in range(n):
        sum += lst[i]
    return sum <= 0
```