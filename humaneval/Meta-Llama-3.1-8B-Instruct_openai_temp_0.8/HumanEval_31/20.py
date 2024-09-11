### Primality Checker
```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Example use cases:

    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    if n <= 1:
        # Prime numbers are greater than 1
        return False
    for i in range(2, int(n**0.5) + 1):
        # Check for divisors up to the square root of n
        if n % i == 0:
            # If n is divisible by i, it's not prime
            return False
    # If no divisors were found, n is prime
    return True

# Test cases
if __name__ == "__main__":
    test_cases = [6, 101, 11, 13441, 61, 4, 1]
    for case in test_cases:
        print(f"{case}: {is_prime(case)}")
```
This script defines a function `is_prime` to check if a given number `n` is prime. The function uses a loop to check for divisors up to the square root of `n`, which is a optimization to reduce the number of iterations. The test cases at the end demonstrate how to use this function.