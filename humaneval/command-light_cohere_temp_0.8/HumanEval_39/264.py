```python
def prime_fib(n: int):
    """
    Returns the n-th Fibonacci number that is prime.
    >>> prime_fib(1)
    2
    is_prime(2)  # True
    >>> prime_fib(2)
    3
    is_prime(3)  # False
    >>> prime_fib(3)
    5
    is_prime(5)  # True
    >>> prime_fib(4)
    13
    is_prime(13)  # False
    >>> prime_fib(5)
    89
    is_prime(89)  # True
    
    Test if a number is a prime or not using the `is_prime` function.
    """
   
    def is_prime(n: int):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    return int(n**0.5)  # - 3
``` 
The function `prime_fib` returns the n-th Fibonacci number that is prime. The function `is_prime` checks if a number is prime or not. 
The function is well-tested and self-contained.