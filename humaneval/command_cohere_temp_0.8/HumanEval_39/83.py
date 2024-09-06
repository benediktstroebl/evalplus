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
    Generates the n-th Fibonacci number that is also prime.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    prev_prime_fib = 3
    current_prime_fib = 5
    count = 0

    while count < n - 2:
        if is_prime(current_prime_fib):
            prev_prime_fib = current_prime_fib
            current_prime_fib = (prev_prime_fib + current_prime_fib) % infinity
            count += 1
        else:
            current_prime_fib = (prev_prime_fib + current_prime_fib) % infinity

    return current_prime_fib

# Note: The above function assumes that the infinity variable is defined somewhere in the scope of the script.

# You can implement the above function using an alternative approach that doesn't rely on the infinite Fibonacci sequence.
```

This script defines a function `prime_fib(n)` that generates the n-th Fibonacci number that is also prime. The function handles cases where n is 1 or 2 differently and includes a recursive helper function `is_prime(n)` to check if a number is prime. 

Note: This code assumes that the `infinity` variable is defined in the script's scope, as used in the modulus operator for handling the infinite Fibonacci sequence. 

This code should be tested to ensure it behaves as expected for various inputs. Feel free to add additional test cases to the `prime_fib` function to cover different scenarios.