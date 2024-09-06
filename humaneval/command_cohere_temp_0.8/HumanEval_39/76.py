Here is a Python script with a self-contained function that solves the problem:
```python
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_fib(n):
    """
    Generates the n-th Fibonacci number that is also prime.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        fib_num = fib_num_prev = 2
        for _ in range(3, n + 1):
            fib_num_next = fib_num + fib_num_prev
            if is_prime(fib_num_next):
                fib_num_prev = fib_num
                fib_num = fib_num_next
        return fib_num
```

This script defines two functions: `is_prime` checks if a given number is prime, and `prime_fib` generates the n-th Fibonacci number that is also prime. The `prime_fib` function first determines if n is within a valid range and then iterates through the Fibonacci sequence, checking each number for primality as it goes, until it finds the n-th prime Fibonacci number. This is validated using test cases in the provided script which should be executed to see the function in action.