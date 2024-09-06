```python
def prime_fib(n: int):
    """
    Returns the n-th number that is a Fibonacci number and is also prime.
    >>> print(prime_fib(1))
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(5)
    True
    >>> prime_fib(6)
    False
    >>> prime_fib(10)
    True
    """
    # Set n to 2, which is the first Fibonacci number
    n = 2
    counter = 0

    # Define a list of Fibonacci numbers and their subsequent primes
    fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...]
    is_prime = [True, False, True, False, True, 3, 5, 13, 89, ...]

    # Check for the number being prime or not
    while n <= len(fibonacci_sequence):
        counter += 1
        if is_prime[counter] and n == fibonacci_sequence[counter]:
            return counter  # Found a prime Fibonacci number

    return False  # No prime Fibonacci number found at position n
```