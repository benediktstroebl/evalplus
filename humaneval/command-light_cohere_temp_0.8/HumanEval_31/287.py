```python
def is_prime(n):
    """
    A function to check whether a number is prime or not.
    """
    accepts an integer 'n' and returns a boolean value (True if n is prime, False otherwise).

    Prime numbers are those that have exactly two distinct divisors: 1 and the number itself, and all other positive integers greater than 2 are divisible by at least 2, 3, 5, ...

    If n <= 1, it is always False
    """

    if n <= 1:
        return False

    # Check if n is 2 or 3
    if n <= 3:
        return True

    # Check if n is a perfect square (up to the 1000th power)
    # to simplify the process, we check if n is power of 2 or 4
    if n % 2 == 0 or n % 4 == 0:
        return True

    # Check for divisibility by primes (up to the sqrt(n)th power)
    sqrt_n = int(math.sqrt(n))
    if sqrt_n > 3:
        # This is because any positive integer greater than 3 can be written as the square of an integer greater than 1
        return True

    # Check for divisibility by numbers 2 and up to sqrt(n)
    for i in range(5, sqrt_n + 1, 6):
        if n % i == 0:
            return True

    return False
```

This function checks if a number is prime or not, it accepts any positive integer `n` and returns a boolean value indicating its primality.

Please note that this is a basic implementation and can be further optimized. Also, note that the function does not yet handle the case of negative numbers or special integers like 0 and 1 properly.