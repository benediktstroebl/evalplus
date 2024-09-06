```python
def prime_fib(n: int):
    if n <= 1:
        return n
    is_prime = [True] * (n - 2)
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i + 1, n, i + 1):
                if is_prime[j]:
                    return j
    return n
```