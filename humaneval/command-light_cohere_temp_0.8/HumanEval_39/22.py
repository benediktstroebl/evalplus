```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        return 2 if is_prime(n) else next((6, n + 1))

def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return False
    return True
```

This script defines a function `prime_fib` that computes the n-th Fibonacci number that is prime and returns the n+1th prime number. The function `is_prime` determines whether a given number n is prime or not using the `isprime` algorithm. 
The `is_prime` function uses a basic algorithm to check primality.