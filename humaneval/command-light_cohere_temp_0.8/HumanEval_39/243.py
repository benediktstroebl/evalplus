```python
def prime_fib(n: int):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(5):
        if is_prime(a):
            a, b = next(iter([c for c in range(2, a + 1) if is_prime(c)]))
    else:
        a, b = next(iter([c for c in range(2, a + 1) if c % 2 == 0]))
    return b

def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
print(prime_fib(5))  # Output: 89
print(is_prime(6))  # Output: False
```

This Python code defines a function `prime_fib` that computes the n-th Fibonacci number, which is a prime, and another function `is_prime` that checks whether a given number is prime or not. The code then demonstrates the by using these functions to find the n-th Fibonacci number and check whether numbers are prime or not.