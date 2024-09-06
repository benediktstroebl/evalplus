```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        limit = 2  # counter
        is_prime = [True] * (n - 1)  # list to store prime factors
        for i in range(2, int(n**0.5)):  # if is_prime[i] and i <= n:
            limit += i
            is_prime[i] = False
        return limit
```