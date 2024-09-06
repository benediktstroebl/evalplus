```python
def prime_fib(n: int):
    if n <= 1:
        return n
    elif n == 2:
        return 2
    elif n % 2 == 0:
        return False
    else:
        a, b = 3, 5
        while b <= n:
            a, b = a + b, b + a
            if b > 1 and a % b == 0:
                return b
            elif b > 1 and a % b == 1:
                return a
```

This script defines a function **prime_fib** that returns the n-th Fibonacci number and is also prime. It uses a common optimization to test for divisibility by checking divisibility of subsequent numbers and returning the first number that is not divisible by the tested number.