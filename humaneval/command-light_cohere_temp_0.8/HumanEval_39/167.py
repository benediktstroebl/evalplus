```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        return 1 if is_prime(n) else (prime_fib(n-1) + 2)

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
This code defines a function `prime_fib` that computes the n-th Fibonacci number that is prime and returns it. The code also defines a function `is_prime` to check if a given number is prime or not. 
The `is_prime` function uses the trial and error algorithm with some optimizations to test for primality.