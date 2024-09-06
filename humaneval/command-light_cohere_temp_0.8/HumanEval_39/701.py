```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 6
    for i in range(3, n+1):
        if is_prime(i):
            return i
    return n

def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
        return False
    return True

print(prime_fib(5))
```