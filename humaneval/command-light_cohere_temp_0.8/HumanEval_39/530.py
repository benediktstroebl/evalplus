```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return prime_fib(n // 2) + 2
    else:
        return prime_fib(n // 2) + next(prime_fibs)

def test_prime_fib():
    print(prime_fib(10))  # Output should be squar of 3 and 3
```