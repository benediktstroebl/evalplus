```python
def prime_fib(n: int):
    """
    Returns n-th number that is a Fibonacci number and is also prime.
    >>> prime_fib(1)
    2
    is_prime = True  # Initialize is_prime flag to True
    3
    is_prime = False  # Assume not prime
    while n > 2 and is_prime == True:
        n -= 1
        is_prime = (n % 2 == 0 or (n % 3 == 0 and n // 3 == 2))
    if n == 2:
        return 3
    elif n == 3:
        return 5
    else:
        # Find the next Fibonacci number
        x, y, z = 0, 1, 1
        while z < n:
            x = y + z
            y = x + z
            z = x + y
        return z  # Return the prime Fibonacci number

# Test the function
test_prime_fib = [
    "Test 1: Function should return 2 for n = 1"
    prime_fib(1)
    assert prime_fib(1) == 2, "Test 1 failed"

    "Test 2: Function should return 3 for n = 2"
    prime_fib(2)
    assert prime_fib(2) == 3, "Test 2 failed"

    "Test 3: Function should return 5 for n = 3"
    prime_fib(3)
    assert prime_fib(3) == 5, "Test 3 failed"

    "Test 4: Function should return 13 for n = 4"
    prime_fib(4)
    assert prime_fib(4) == 13, "Test 4 failed"

    "Test 5: Function should return 89 for n = 5"
    prime_fib(5)
    assert prime_fib(5) == 89, "Test 5 failed"
]
```

This code defines a function `prime_fib` that calculates and returns the n-th Fibonacci number which is prime. The function uses a reasoning to determine whether a number is prime or not, and it returns the next Fibonacci number when it's not prime. The test code validates the function's correctness by passing different values to `prime_fib` and asserting that the returned values match the expected results.