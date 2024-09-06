```python
def triples_sum_to_zero(l: list):
    n = len(l)
    for i in range(n):
        a = l[i]
        for j in range(i + 1, n):
            b = l[j]
            for k in range(j + 1, n):
                c = l[k]
                if a + b + c == 0:
                    return True
                elif c < 0:
                    b -= c
                else:
                    return False
    return False
```