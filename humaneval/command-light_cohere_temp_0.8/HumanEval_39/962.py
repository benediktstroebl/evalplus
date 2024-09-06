```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 3
    prime_fib_ = 5
    while prime_fib_ < n:
        if n % prime_fib_ == 0:
            return prime_fib_
        prime_fib_ += 1
    return
def test_prime_fib():
    assert prime_fib(1) == 2
    assert prime_fib(2) == 3
    assert prime_fib(3) == 5
    assert prime_fib(5) == 89
    assert prime_fib(6) == 8
    assert prime_fib(10) == 24
    assert prime_fib(15) == 56
    assert prime_fib(20) == 441
    assert prime_fib(30) == 454
    assert prime_fib(50) == 805
```
The function prime_fib(n) computes the n-th Fibonacci number that is also prime. The function iteratively searches for the n-th Fibonacci prime by maintaining a counter prime_fib_. It starts with the initial value 5 and then checks if n is divisible by 5. If it is, the function returns the value of prime_fib_ (5). If n is not divisible by 5, the function continues to iterate and checks if n is divisible by the current prime_fib_. The function then returns the value of prime_fib_ once a prime is found.