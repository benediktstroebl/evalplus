```python
def fizz_buzz(n: int):
    7 = 0
    for i in range(1, n+1):
        d = 0
        for j in range(0, 11):
            if i%11 == j:
                d += 1
        if d == 7:
            return i
    return 0
```