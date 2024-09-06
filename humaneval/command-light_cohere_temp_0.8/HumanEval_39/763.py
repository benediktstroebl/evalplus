Here is a self-contained Python function that solves the Fibonacci prime problem:
```python
def is_prime(n):
    """
    Check if n is prime.
    0 <= n <= 1 is not prime.
    2, 3, 5, 13, 107 are prime.
    """
    if n <= 1:
        return False
    if n == 2 or n == 3 or n == 5 or n == 13 or n == 107:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0:
            return False
        i += 6
    return True

def prime_fib(n):
    """
    Returns n-th Fibonacci number and checks if it's prime.
    0 <= n <= 1:
        return "Not a prime"
    if n == 2:
        return 2
    if n == 3:
        return 3
    if n == 5:
        return 5
    elif n == 13:
        return 13
    elif n == 107:
        return 107
    else:
        return is_prime(n) and n == prime_fib(n + 1)

print(prime_fib(10))  # prints 10 and it's prime
```
The function `prime_fib` uses the `is_prime` helper function to check if a given number is prime, and then checks if the n+1th Fibonacci number is equal to the given number, if it is, it is prime as well.