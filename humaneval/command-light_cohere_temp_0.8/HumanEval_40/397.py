```python
def triples_sum_to_zero(l: list):
    n = len(l)
    for i in range(n // 3):
        left, middle, right = i * 3, i * 3 + 1, i * 3 + 2
        if sum(l[left:right]) == 0:
            return True
        elif i == n // 3 - 1:
            return False
    return True
```