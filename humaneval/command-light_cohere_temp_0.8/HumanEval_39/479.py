```python
def prime_fib(n: int):
    """
    Returns the n-th number that is a Fibonacci number and is also prime.
    >>> prime_fib(1)
    2
    is_prime: True
    """
    # Define Fibonacci sequence up to nth number
    fib_sequence = [0, 1]
    for i in range(2, n+1):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    # Define is_prime helper function
    def is_prime(n):
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
    # Return the n-th Fibonacci number that is prime
    return fib_sequence[n - 1] if is_prime(fib_sequence[n - 1]) else -1
```
This code defines a prime_fib function that computes the n-th Fibonacci number that is prime. 
The Fibonacci sequence is defined as a list, with the first two elements being 0 and 1. The sequence is then computed using a for loop, with each iteration adding the last two elements. The function then defines an helper function is_prime that checks if a number is prime or not. It returns True if the is prime and returns -1 otherwise. The function finally returns the value of the n-th Fibonacci number that is prime.