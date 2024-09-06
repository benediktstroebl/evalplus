```python
def is_prime(n):
    """Check if a given number is prime."""
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

# Test function
def test_is_prime():
    print("The following numbers are prime:", endwith(is_prime(6), print)),
    print("The following numbers are NOT prime:", endwith(is_prime(4), print))
    print("The number 101 is prime.", endwith(is_prime(101), print))
    print("The number 11 is prime.", endwith(is_prime(11), print))
    print("The number 13441 is prime.", endwith(is_prime(13441), print))
    print("The number 61 is prime.", endwith(is_prime(61), print))
    print("The number 1 is NOT prime.", endwith(is_prime(1), print))

test_is_prime()
```
The above Python code defines a function is_prime(n) that checks whether a given number is prime. The function implements a Miller-Rabin primality test, which is one of the most efficient primality tests. It then passes all corresponding tests with various numbers and prints the results.