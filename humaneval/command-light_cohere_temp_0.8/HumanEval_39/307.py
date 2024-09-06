```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    factors = []
    for i in range(3, n + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            factors.append(i)
    return next(factors)

# Test the function
print(prime_fib(5))
``` 
This code defines a function `prime_fib` that calculates the n-th Fibonacci number and returns it if it's prime. It also returns the region of primes that are less than or equal to `n`.