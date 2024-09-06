```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    is_prime = [True, False, True]
    for i in range(2, n+1):
        is_prime[i % 2] = False
    for j in range(3, n+1, 2):
        if is_prime[j]:
            for k in range(j * j, n+1, j):
                is_prime[k] = True
                if k == n:
                    return k
    return None
```