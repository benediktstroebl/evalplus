Here's a Python script with a self-contained function `prime_fib` that generates the n-th number that is a Fibonacci number and it's also prime:
```python
def is_prime(n):
    """
    is_prime checks if a number is prime
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
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer.")
    if n <= 2:
        return 2 if n == 1 else 3
    fib_nums = [0, 1]
    for i in range(2, n + 1):
        fib_nums.append(fib_nums[i - 1] + fib_nums[i - 2])
    for _ in range(3, n + 1):
        if is_prime(fib_nums[_]):
            return fib_nums[_]
    return fib_nums[n - 1]

# Tests
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
```

This script defines two functions:
- The `is_prime` function checks if a given number is prime. It handles some special cases (if the number is less than or equal to 1 it returns False, if the number is 2 or 3 it returns True) and then uses a straightforward algorithm involving modulo arithmetic to check for primality.
- The `prime_fib` function calculates the n-th Fibonacci number that is also a prime number. It does so by first handling some edge cases (checking if n is less than or equal to 2) and then iteratively calculating the Fibonacci sequence, checking each number for primality as it goes. 

The script also includes tests to verify the function behavior. You can modify the `prime_fib` function call parameters with other positive integers to test other cases.