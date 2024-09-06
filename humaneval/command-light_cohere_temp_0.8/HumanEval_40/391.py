```python
def triples_sum_to_zero(l):
    if not_three_sum(l):
        return True
    return False

def not_three_sum(l):
    n = len(l)
    for i in range(n // 3):
        for j in range(i + 1, n // 3):
            if l[j] > l[i] and l[j] > l[j + 1]:
                return [l[i], l[j], l[j + 1]]
    return []
```