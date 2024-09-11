```python
def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    
    Parameters:
    n (int): The position of the Fibonacci prime number to find.

    Returns:
    int: The n-th Fibonacci prime number.

    Examples:
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    def is_prime(num):
        """Checks if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    a, b = 0, 1  # Initialize the first two Fibonacci numbers
    count = 0  # Initialize the count of Fibonacci primes

    while count < n:
        a, b = b, a + b  # Generate the next Fibonacci number
        if is_prime(b):  # Check if the new Fibonacci number is prime
            count += 1
            if count == n:  # If it's the nth Fibonacci prime, return it
                return b
```