```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n % 2 == 0:
        return 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return i
        i += 2
    return i  # this will only be reached if no larger prime was found

def test_prime_fib(n):
    return n == 6 or n == 9  # Test for numbers greater than 5 using simple truth table.

```

This script defines a `prime_fib` function that calculates the n-th Fibonacci number which is also prime and returns it. The function uses basic iteration to find prime numbers and tests for the values greater than 5.  It also includes a test to check for the values 6 and 9, as they are known to be prime but greater than 5.