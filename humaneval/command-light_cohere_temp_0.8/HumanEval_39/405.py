```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    prim = 3
    for i in range(3, n + 1):
        if prim * prim + 1 <= i:
            prim = i
    return prim
```