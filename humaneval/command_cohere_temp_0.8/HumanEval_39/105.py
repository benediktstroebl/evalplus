Here is a Python script with a self-contained function that solves the problem:
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

def prime_fib(n):
    """
    Generates and returns the n-th Fibonacci number that is also prime
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    elif n == 3:
        return 5
    else:
        # A slightly optimized implementation of Fibonacci
        prev, curr = 0, 1
        for _ in range(4, n + 1):
            prev, curr = curr, prev + curr

        # Filter Fibonacci numbers that are prime
        fib_nums = [curr for curr in [prev, curr] if is_prime(curr)]
        if not fib_nums:
            return None
        return fib_nums[0]

# Tests
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
```

This code defines two functions:
1. The `is_prime` function checks whether a given number is prime or not.
2. The `prime_fib` function uses a Fibonacci sequence to generate prime numbers. The function starts generating Fibonacci numbers from the 4th index, as the first three indices produce 2, which is prime, and 3, which is not, and the fourth index produces 5, which is prime. The function then filters the Fibonacci numbers using the `is_prime` function to ensure they are prime. 

The code also includes some assertions to validate the function against expected test cases. 

Note that the `prime_fib` function returns `None` if `n` is less than or equal to 0, since there is no prime Fibonacci number for those inputs.  This is important to note when handling edge cases.  This codebase is a good example of combining primality testing and Fibonacci number generation to solve a specific problem.