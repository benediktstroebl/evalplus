```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 1
    if n % 3 == 0:
        return 3
    # To find the next prime, check factors up to the square root of sqrt(n) + 1
    for i in range(5, int(sqrt(n) ** 0.5) + 1, :
        if n % i == 0:
            return i
def test_prime_fibonacci(n):
    return prime_fib(n) == n
```