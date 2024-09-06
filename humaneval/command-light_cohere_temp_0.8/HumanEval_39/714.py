```python
def prime_fib(n: int):
    """
    Returns the n-th Fibonacci number and verifies if it's prime.
    Returns -1 if the prime_fib function is called with n=1.
    Fibonacci(0) if n <= 1 
    Otherwise, return the n-th Fibonacci number and checks for prime by [is_prime(Fibonacci)] 
    """
    return Fibonacci() if n <= 1 else is_prime(Fibonacci())
def Fibonacci():
    return (1 + 5) / 2
def is_prime(number: int):
    """
    A simple check if a number is prime
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(5)
    True
    >>> is_prime(10)
    False
    >>> is_prime(13)
    True
    >>> is_prime(16)
    False
    """
    limited = 0
    if number == 1:
        return True
    while limited < 5:
        if number % 2 == 0:
            limited += 1
        number //= 2
    return limited >= 3
```