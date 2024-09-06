```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    is_prime = [True] * (5 * (n - 4))
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            is_prime[i::2::i] = False
    for i in range(2, n + 1):
        if is_prime[i]:
            return i
    return n
```