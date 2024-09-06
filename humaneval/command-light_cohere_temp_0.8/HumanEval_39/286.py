```python
def prime_fib(n: int):
    """
    Returns the n-th Fibonacci number that is prime.
    >>> prime_fib(1)
    2
    is_prime = True 
    while(is_prime == True):
        if (fibonacci(n) == 1):
            is_prime = False  # False is not prime
        else:
            continue 
    return fibonacci(n)
def is_prime(n: int):
    """
    Checks if n is prime.
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(5)
    True
    >>> is_prime(7)
    False
    >>> is_prime(8)
    True
    >>> is_prime(9)
    False
    """
    limit =  6 
    while(n <= limit):
        if (n % 2 == 0 or n % 3 == 0):
            return False 
        n += 1 
    return True
def fibonacci(n: int):
    """
    Returns n-th Fibonacci number
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
prime_fib(5)  # Test the function
print(is_prime(7))  # Test the is_prime function
 ```
This Python script defines a self-contained function `prime_fib` that returns the n-th Fibonacci number which is also prime. The function uses a is_prime function to check if the number passed as an argument is prime or not.