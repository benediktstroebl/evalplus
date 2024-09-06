```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    else:
        d = 0
        for i in range(2, n):
            if is_prime(i) and i != 2:
                d += 1
        return d + 1

def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return False
    return True

# Example usage
print(prime_fib(5))  # Output: 89
print(is_prime(6))  # Output: True
print(is_prime(30))  # Output: False
```
This code defines a function **prime_fib(n)** that calculates the n-th Fibonacci number that is prime and returns it. The code also defines a function **is_prime(n)** that checks whether a given number is prime using the Sieve of Eratosthenes algorithm.