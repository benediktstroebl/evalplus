```python
def prime_fib(n: int):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(5):
        a, b = next( (a, b) )
        if a == b:
            continue
        if a > 1 and is_prime(a):
            yield a
        if b > 1 and is_prime(b):
            yield b

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

# Example of calling the function
print(prime_fib(5))
``` 
This code defines a `prime_fib` function that calculates the n-th Fibonacci number that is prime, and a `is_prime` function to check if a number is prime. The `prime_fib` function uses an iterative approach with candidate numbers to find prime numbers. The `is_prime` function uses a simple algorithm to check for prime numbers.