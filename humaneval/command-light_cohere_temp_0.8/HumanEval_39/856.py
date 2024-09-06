```python
def prime_fib(n: int):
    if n <= 1:
        return n
    is_prime = [True] * (n - 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
                if j == n or is_prime[j] == True:
                    break
    return n
```