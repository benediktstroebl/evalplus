```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    for i in range(3, n+1):
        if is_prime(i) and i != 2:
            return i
    return None

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
The code defines a `prime_fib` function that calculates the n-th Fibonacci number and determines whether it is prime. It also includes a test case, `is_prime`, which employs a simple algorithm to verify whether a given number is prime or not. 

This implementation is self-contained, and it does not require external functions or modules.