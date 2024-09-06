```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    prim = 3
    while prim * prim <= n:
        if prim > 1 and prim % 1 == 0:
            return prim
        prim += 1
    return prim
```