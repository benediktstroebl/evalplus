Here is a self-contained Python script with a function that solves the problem of finding the n-th Fibonacci number and checks if it is also prime:

```python
def is_prime(n):
    """Return True if n is a prime number, else False."""
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

def prime_fib(n):
    """Return the n-th Fibonacci number and verify if it's prime."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n % 2 == 0:
        return 2
    fib = 0
    fib_prime = 1
    for i in range(2, n + 1):
        if is_prime(i) and fib_prime <= i:
            fib = i
            fib_prime = i
        else:
            break
    return fib

print(prime_fib(10))  # Should print a Fibonacci number and it's prime.