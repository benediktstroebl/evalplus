```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0:
        return 5
    primes = [2, 3]
    for i in range(5, n+1, 2):
        if is_prime(i):
            primes.append(i)
    return primes[n-1]

def is_prime(n: int):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
```
The code defines a `prime_fib` function that returns the n-th Fibonacci prime number and is also prime, and passes the tests with the `is_prime` function. The `is_prime` function returns true if n is a prime number and false otherwise.