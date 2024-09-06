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
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    # Initialize two variables for the first two fibonacci numbers
    a, b = 0, 1
    count = 0

    while True:
        # Check if the next fibonacci number is prime
        if is_prime(a):
            count += 1
            if count == n:
                break
        a, b = b, a + b

    return a

# Tests
assert prime_fib(1) == 2
assert prime_fib(2) == 3
assert prime_fib(3) == 5
assert prime_fib(4) == 13
assert prime_fib(5) == 89
```

This script defines a `prime_fib` function that generates the n-th Fibonacci number that is also prime. It uses a `is_prime` function to check if a number is prime. In the `prime_fib` function, it initializes two variables `a`, `b` for the first two Fibonacci numbers. It then enters a while loop and checks if the next Fibonacci number is prime using the `is_prime` function. If it's prime, it increments the count and checks if it's the n-th prime Fibonacci number. If so, it breaks out of the loop and returns that number. The test assertions show the function passing for test cases 1 through 5. 

This solution is efficient and will not exhaust the stack because it uses an iterative process to calculate and check for primality, avoiding the risk of reaching maximum recursion depths. 

This solution delivers the n-th Fibonacci prime number efficiently and correctly.