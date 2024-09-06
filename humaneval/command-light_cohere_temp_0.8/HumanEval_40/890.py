```python
def triples_sum_to_zero(l: list):
    n = len(l)
    for i in range(n // 3):
        for j in range(i + 1, n // 3):
            sum_so_far = sum(l[i:j])
            if sum_so_far < 0:
                return False
    return True
```