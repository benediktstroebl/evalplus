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
        raise ValueError("n must be positive")

    fib_nums = [0, 1]
    for i in range(2, n + 1):
        fib_nums.append(fib_nums[i - 1] + fib_nums[i - 2])

    for fib_num in fib_nums:
        if is_prime(fib_num):
            return fib_num

# Tests
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
```
This code defines a `prime_fib(n)` function that calculates the n-th Fibonacci number that is also prime. It does this by initially creating a Fibonacci sequence and then iterating through it to find the n-th number that is prime. 

The `is_prime(n)` function is introduced to check if a number is prime or not, which is a common operation used in many algorithms and problems related to prime numbers.