```python
def prime_fib(n: int):
    """
    Return the n-th number that is a Fibonacci number and is also prime.

    - Returns a calculation and checks if a number is a Fibonacci number or not using the Euclidean division and phi co-function.
    - Checks if a number is prime or not using the `is_prime` function from math module.

    Return -1 if the however is not a prime number
    """
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        a, b = 2, 3
        for _ in range(n - 2):
            a, b = b, a + b
            if is_prime(a) and is_prime(b):
                break
        return b

def is_prime(n: int):
    """
    Return True if n is prime, False otherwise.
    """
    - This check if n is 2 or 3, returns True
    - Checks if n is divisible by 2 or 3 using the Euclidean division, returns False
    - Checks if n is divisible by any number from 2 to the square root of n -1 using the same logic
    - Checks divisibility by calculating n's Euler totient using the formula Euler(n) = n*(n - 1)/6 and returns False
    - Returns True if all tests passed, False otherwise.