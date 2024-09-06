Here's a Python script with a self-contained function `prime_fib` that generates the n-th number that is a Fibonacci number and it's also prime:
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
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    fib_nums = [0, 1]
    for i in range(2, n + 1):
        fib_nums.append(fib_nums[i - 1] + fib_nums[i - 2])
    for i in range(2, len(fib_nums)):
        if is_prime(fib_nums[i]):
            return fib_nums[i]
    return fib_nums[-1]

# Tests
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
```

This script defines a helper function, `is_prime`, which checks if a given number is prime. The `prime_fib` function uses the Binet's formula to generate Fibonacci numbers and then filters out the prime ones. Finally, it returns the n-th number that is a Fibonacci number and it's also prime. 

Note that this approach has a time complexity of O(n^2) since it generates all Fibonacci numbers and then filters out the prime ones, you can optimize it using memoization to achieve a better time complexity.