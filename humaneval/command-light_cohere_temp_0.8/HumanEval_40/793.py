```python
def triples_sum_to_zero(l: list):
    n = len(l)
    for i in range(n // 3):
        sum_left = sum(l[i:i + n // 3])
        sum_right = sum(l[i + n // 3:])
        total = sum_left + sum_right
        if total < 0:
            return False
    return True
```