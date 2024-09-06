```python
def prime_fib(n: int):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(5):
        if is_prime(a):
            a = b
        b += 1
    return a

def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return False
    return True
``` 
This code defines a prime_fib function that calculates the n-th Fibonacci number which is also a prime, and a related is_prime function that returns True if a given number is prime, and False otherwise.