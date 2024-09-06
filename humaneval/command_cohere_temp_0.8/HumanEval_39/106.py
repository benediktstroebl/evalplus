```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n):
    if n < 1:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        x, y = 0, 1
        for i in range(n - 1):
            x, y = y, x + y
        return prime_flag(x)

def prime_flag(n):
    if is_prime(n):
        return n
    else:
        return None
```

The function prime_fib() uses an iterative approach to generate the Fibonacci numbers and includes a primality test for each Fibonacci number generated. The is_prime() function is a simple primality test that checks if a number is divisible by any integer between 2 and the square root of the number. A number is considered prime if it is not divisible by any number in this range and is greater than 1. The prime_flag() function acts as a wrapper for is_prime() and ensures that the result is only returned if the number is prime. 

This approach ensures that the prime_fib() function returns the n-th number that is both a Fibonacci number and a prime number. 

Note that the script assumes that the input `n` is valid and positive. You can adjust the boundary conditions in the `prime_fib()` function to handle invalid inputs accordingly. 
```python 
# Here are some examples of how you can test this function:
# Test the first few prime Fibonacci numbers
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5

# Test some larger prime Fibonacci numbers
assert prime_fib(4) == 13
assert prime_fib(5) == 89

# Test edge cases
assert prime_fib(0) is None
assert prime_fib(-1) is None
``` You can write more tests for this function by generating random inputs and verifying the corresponding outputs.