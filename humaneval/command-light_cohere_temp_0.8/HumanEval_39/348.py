```python
def prime_fib(n: int):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(5):
        if is_prime(a):
            a, b = next(b for b in range(2, a+1) if is_prime(b))
    return b

def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
        return False
    return True

# Test the prime_fib function
print(prime_fib(6))  # Output should be 6
print(prime_fib(7))  # Output should be 5
```