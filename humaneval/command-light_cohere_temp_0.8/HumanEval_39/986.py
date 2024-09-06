```python
def prime_fib(n: int):
    if n <= 1:
        return n
    is_prime = [True] * (n - 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
    return is_prime[-1]
```
This function, `prime_fib`, determines whether a given number `n` is the n-th Fibonacci number that is also prime. The method is similar to that of Euclid, using the list comprehension approach.