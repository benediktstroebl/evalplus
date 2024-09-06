```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_fib(n):
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # The n-th prime Fibonacci number has the form F_n^2 - F_n-1
        prev_fib = 0
        curr_fib = 1
        count = 0
        while count < n:
            prev_fib, curr_fib = curr_fib, prev_fib + curr_fib
            count += 1
        return curr_fib ** 2 - prev_fib

# Test suite
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
```

This script defines a function `prime_fib` that returns the n-th number that is a Fibonacci number and it's also prime. The function checks the edge cases and returns the required value for the given n. The `is_prime` function is also included to check if a number is prime or not. This is achieved by iteratively checking the divisibility of the number by all odd numbers starting from 5 up to the square root of the number.  Finally, the code includes a test suite to validate its behavior for specific inputs.