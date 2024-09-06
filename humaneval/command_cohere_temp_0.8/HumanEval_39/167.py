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

def prime_fib(n):
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # Iterate through Fibonacci numbers and check if each number is prime
        count = 0
        a, b = 0, 1
        while count < n:
            x = a + b
            if is_prime(x):
                if count == n - 1:
                    return x
                count += 1
            a, b = b, a + b

# Test suite
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
```

This script defines a `prime_fib` function that calculates the n-th Fibonacci number that is also prime. It does this by maintaining two variables `a` and `b` as Fibonacci numbers and checking if each number is prime with an `is_prime` function. 

The `is_prime` function is also included to check if a given number is prime. It efficiently checks primality by starting from 5 and increasing in 6 steps. If the number is divisible by 2 or 3, it returns immediately. Otherwise, it checks if the number is divisible by any odd number starting from 5 through a loop. 

The script also includes a test suite to verify the correctness of the `prime_fib` function. You can remove the comments on the test assertions to execute them and see the function's behavior for different test cases.  This will ensure its correctness against specific test cases.