```python
def triples_sum_to_zero(lst):
    n = len(lst)
    for i in range(n):
        sum_to_zero = lst[i] + lst[(i+1) % n] + lst[(i+2) % n]
        if sum_to_zero < 0:
            return True
    return False
```