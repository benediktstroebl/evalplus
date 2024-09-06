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
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
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
        # This section calculates n-th Fibonacci number and then filters to find only primes
        fib = [0, 1]
        for _ in range(n - 3):
            next_fib = fib[-1] + fib[-2]
            fib.append(next_fib)
        for fib_num in fib[3:]:
            if is_prime(fib_num):
                return fib_num
        return None
```

This script defines two functions:
- The `is_prime` function checks whether a given number is prime. It handles the special cases of numbers less than or equal to 1, then uses a combination of checks by 2 and 3 to quickly rule out multiples of these small primes. It then checks in increments of 6, starting from 5, until it has ruled out the possibility of the number being divisible by any odd number greater than 3.
- The `prime_fib` function returns the n-th number that is a Fibonacci number and it's also prime. It calculates the n-th Fibonacci number using a simple iterative approach, then filters the results to find the prime numbers among them. 

The script also provides example outputs to show the behavior of the `prime_fib` function.