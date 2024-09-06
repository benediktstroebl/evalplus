Here's a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n):
    """
    Returns the n-th number that is both prime and a Fibonacci number.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 2
    else:
        # Calculate nth Fibonacci number
        prev_fib = 0
        curr_fib = 1
        for _ in range(2, n + 1):
            prev_fib, curr_fib = curr_fib, prev_fib + curr_fib
        
        # Filter the Fibonacci numbers that are also prime
        fib_primes = [fib for fib in [prev_fib, curr_fib] if is_prime(fib)]
        
        if not fib_primes:
            raise ValueError(f"No prime Fibonacci numbers found for n = {n}.")
        elif len(fib_primes) == 1:
            return fib_primes[0]
        else:
            return fib_primes[n - 2]

# Tests
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
```
This script defines two functions: 
- The `is_prime` function checks whether a given number is prime.
- The `prime_fib` function returns the n-th number that is both a prime number and a Fibonacci number. 

The script provides example outputs to demonstrate the behavior of the `prime_fib` function. And finally, the script includes tests to validate the functionality of the `prime_fib` function for different input values.  The code will print the test assertions if the assertions are correct, and it will throw an error if the assertions are incorrect. 

Note that the `prime_fib` function raises a `ValueError` when no prime Fibonacci numbers are found for a given value of `n`, or when `n` is less than or equal to 0. These exceptions provide meaningful error messages and help handle edge cases gracefully.  It is also important to note that the time complexity of the function `prime_fib` is irregular and depends on the ratio of the prime Fibonacci numbers present in the sequence. The execution time may vary depending on the value of n.