```python
import math

def prime_fib(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n % 2 == 0:
        return math.sqrt(5) + 1
    else:
        return prime_fib(n // 2) + prime_fib(n - 2)

# Unit tests
def test_prime_fib():
    assert prime_fib(1) == 1
    assert prime_fib(2) == 2
    assert prime_fib(3) == 5
    assert prime_fib(4) == 13
    assert prime_fib(5) == 89
    assert prime_fib(6) == 6
    assert prime_fib(7) == 8
    assert prime_fib(8) == 24
    assert prime_fib(9) == 36
    assert prime_fib(10) == 340
    assert prime_fib(11) == 559
    assert prime_fib(12) == 5516
    assert prime_fib(13) == 89

    assert prime_fib(14) == 26
    
    assert prime_fib(15) == 55
    assert prime_fib(16) == 16
    assert prime_fib(17) == 17
    assert prime_fib(18) == 56
    assert prime_fib(19) == 232
    assert prime_fib(20) == 441
```
The function `prime_fib` uses an iterative algorithm to find the n-th Fibonacci number that is prime, while `test_prime_fib` is a function that tests the `prime_fib` function with a set of values.

This is just one possible way to solve the problem, and you can always find other methods and algorithms for solving the same problem.