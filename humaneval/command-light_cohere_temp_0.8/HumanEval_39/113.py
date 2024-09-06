```python
def prime_fib(n: int):
    if n <= 1:
        return n
    for i in range(2, n+1):
        if is_prime(i) and not_prime(i+2):
            return i
    return n

def is_prime(n: int):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
        return False
    return True

def not_prime_factorize(n: int):
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, ]:
        if n % i == 0 and is_prime(i):
            factors.append(i)
            n = n // i
    return factors

def prime_fibonacci(n: int):
    return prime_fib(n)[-]
n = int(input("Enter a number to find prime Fibonacci: "))
print(f"nth Fibonacci number is {prime_fibonacci(n)}")
```