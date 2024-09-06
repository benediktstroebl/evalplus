```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    prime_fib = 3
    is_prime = True
    while is_prime:
        if n % prime_fib == 0:
            return 0
        prime_fib += 1
        is_prime = n % prime_fib == 0
    return

print(prime_fib(5))  # This should output 89
```