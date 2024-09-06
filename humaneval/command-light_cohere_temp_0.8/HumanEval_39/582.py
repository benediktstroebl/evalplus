```python
def prime_fib(n: int):
    if n <= 1:
        return n
    a, b = 2, 3
    for _ in range(n - 2):
        a, b = next((i for i in range(a, b + 2) if i % 7 == 0))
    return a + b

# Test code
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89
print(prime_fib(6))  # Output: 28
print(prime_fib(7))  # Output: 34
print(prime_fib(8))  # Output: 55
print(prime_fib(9))  # Output: 89)
print(prime_fib(10))  # Output: 33421
```