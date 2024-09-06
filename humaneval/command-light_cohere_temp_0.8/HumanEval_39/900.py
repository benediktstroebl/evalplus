```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    else:
        # Use Sieve of Eratosthenes algorithm to find primes
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(3, int(n**0.5) + 1,:
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return next(i for i in primes if i == n)

# Example usage
print(prime_fib(5))
 ```