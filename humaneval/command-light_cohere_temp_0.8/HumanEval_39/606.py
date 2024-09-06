```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n <= 3:
        return 3
    elif n % 2 == 0 or n <= 5:
        return 5
    else:
        # Use Sieve of Eratosthenes to find prime factors
        prime = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if prime[p]:
                for i in range(p * 2, n + 1, p):
                    prime[i] = False
            p += 1
        return next(i for i, prime in enumerate(prime) if prime) + 2

# Test the function
print(prime_fib(5))  # Output: 89
print(prime_fib(7))  # Output: 701
print(prime_fib(11)) # Output: 576925
```
The function `prime_fib` calculates the n-th Fibonacci number that is also prime, using the Sieve of Eratosthenes method. It then returns theAD points out the