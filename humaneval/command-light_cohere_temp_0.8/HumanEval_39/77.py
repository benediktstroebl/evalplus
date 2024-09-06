```python
def prime_fib(n: int):
    if n <= 1:
        return n
    is_prime = [True] * (n - 1)
    for i in range(2, int(n**0.5 / 2):
        if is_prime[i] == True:
        for j in range(i + 1, n, i):
            if is_prime[j] == True:
                return i
    return n
```