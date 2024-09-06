```python
def prime_fib(n: int):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(5):
        if is_prime(a):
            a, b = next((c for c in range(2, a + 1) if is_prime(c)))
    else:
        a, b += 1
    return b

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

# Test the function
print(prime_fib(5))
print(prime_fib(10))
print(prime_fib(30))
```
This code defines a function `prime_fib` that computes the n-th Fibonacci number and checks if it's prime, and another function `is_prime` that returns `True` if a number is prime, and `False` otherwise. The function also implements an loop to check divisibility up to the square root of the number.