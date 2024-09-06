```python
def prime_fib(n: int):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(5):
        a, b = next( (a, b) for a in range(2) for b in range(2) if is_prime(a) )
    return b

def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
        return False
    return True

# Test cases
print(prime_fib(1))      # 2
print(prime_fib(2))      # 3
print(prime_fib(3))      # 5
print(prime_fib(5))      # 89
print(prime_fib(6))      # 6)
print(prime_fib(7))      # No solution, 7 is not prime
print(prime_fib(11))    # No solution, 11 is not prime
print(prime_fib(100)) # No solution, 100 is not prime

```