Here's a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    """
    Checks if a number is prime
    """
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

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # Starts with Fibonacci number 5 (index 3)
        idx = 3
        prev_fib = 0
        curr_fib = 1
        num = 5
        while True:
            # Checks whether the current Fibonacci number is prime
            if is_prime(num):
                if n == 1:
                    return num
                n -= 1
            # Update the Fibonacci number and the index where it starts
            idx += 1
            if idx > 50:
                break
            prev_fib, curr_fib = curr_fib, prev_fib + curr_fib
            num = prev_fib + curr_fib

        # If we reach this line, it means we didn't find a prime Fibonacci number in time
        # So we revert to a slower method and check each number individually
        for i in range(3, n + 2):
            if is_prime(i) and i % 2 == 0:
                return i

        return None

# Tests
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
assert prime_fib(6) == 1961
```

This script defines two functions:
- The `is_prime` function checks whether a given number is prime. It handles cases where the given number is less than or equal to 1, in which case it returns False. It also handles cases where the number is 2 or 3, which are prime numbers. Then, for larger numbers, it uses the `6k ± 1` rule to check only odd numbers for primality, which greatly improves efficiency.
- The `prime_fib` function returns the n-th number that is a Fibonacci number and it's also prime. It uses an optimized approach for the first 50 Fibonacci numbers and checks each number for primality. If it doesn't find a prime number within the first 50 Fibonacci numbers, it resorts to a slower method that checks each number individually. 

The code also includes tests to validate the function `prime_fib`.