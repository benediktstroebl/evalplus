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

def prime_fib(n: int):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n should be a positive integer")
    
    count = 0
    fib_n = 0
    fib_prev = 1
    while count < n:
        fib_next = fib_prev + fib_n
        if is_prime(fib_next):
            nth_prime_fib = fib_next
            count += 1
        fib_prev = fib_n
        fib_n = fib_next
    return nth_prime_fib

# Tests
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
```

This script defines a function `prime_fib` that generates the n-th number that is a Fibonacci number and it's also prime. The function first generates the Fibonacci sequence until the n-th index. Then, it checks if each number in the sequence is prime using the `is_prime` function. If it finds the n-th prime number in the sequence, it returns it. If not, the function will continue generating the sequence. The `is_prime` function is also provided, which checks if a given number is prime or not using the trial division method optimized for efficiency. 

Note that generating primes in the Fibonacci sequence is a highly unbalanced process, so the `prime_fib` function may return much larger numbers than expected for small input `n`.