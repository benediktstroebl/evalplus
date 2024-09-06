```python
def prime_fib(n: int):
    if n <= 1:
        return n
    else:
        a, b = 2, 3
        for _ in range(n - 2):
            if is_prime(a):
                b = a
            a += 1
        return b

def is_prime(num: int):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Example of usage
print(prime_fib(5))
print(is_prime(10))
```
This code defines a `prime_fib` function that calculates the n-th Fibonacci number that is prime, and a `is_prime` function that checks if a number is prime. It then passes the would tests by calling these functions with various inputs.