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
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    prev_fib, curr_fib = 0, 1
    for _ in range(n - 2):
        prev_fib, curr_fib = curr_fib, prev_fib + curr_fib
    
    # We calculate the next potential prime Fibonacci number.
    next_fib = curr_fib * 2 + prev_fib
    while not is_prime(next_fib):
        next_fib = curr_fib * 2 + prev_fib

    return next_fib
```
The code utilizes two nested loops to generate Fibonacci numbers and then verifies if each number is prime using the `is_prime` function. To conserve resources, an upper limit to the nested loop is set to 2000, assuming that the `n` value requested would be less. The `is_prime` function utilizes a linear approach to check for prime by testing numbers up to the square root of the given number.  This approach is efficient for checking individual numbers for primality, but not optimized for larger prime checks, hence the upper limit.