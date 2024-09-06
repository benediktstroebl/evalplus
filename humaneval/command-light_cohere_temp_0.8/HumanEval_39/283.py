```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    # 2 and 3 are prime
    for i in range(4, n + 1):
        if n % i == 0:
            return i
def test_prime_fib():
    assert prime_fib(5) == 89
    assert prime_fib(2) == 2
    assert prime_fib(0) == 0
    assert prime_fib(10) == 24
    assert prime_fib(15) == 1683
    assert prime_fib(16) == 8
    assert prime_fib(17) == 17
    assert prime_fib(48) == 1361
    assert prime_fib(23) == 89
    assert prime_fib(97) == 233
    assert prime_fib(364) == 2940
    assert prime_fib(IONA) == 4509
```
The code defines a function called `prime_fib` that returns the n-th Fibonacci number that is prime. The function first checks if n is less than 1 and returns n itself if true. It then checks if n is even and returns 2. If n is 4, 5, or 6, the function returns the corresponding Fibonacci number. It then iterates through the unique prime numbers starting from i = 4 and checks if n is divisible by each number. The function returns the unique prime number that is the i-th prime.