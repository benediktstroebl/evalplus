```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

    Parameters:
    n (int): The number to check for primality.

    Returns:
    bool: True if n is prime, False otherwise.
    """
    if n <= 1:  # Prime numbers are greater than 1
        return False
    if n <= 3:  # 2 and 3 are prime numbers
        return True
    if n % 2 == 0 or n % 3 == 0:  # If n is divisible by 2 or 3, it's not prime
        return False
    i = 5
    while i * i <= n:  # We only need to check up to the square root of n
        if n % i == 0 or n % (i + 2) == 0:  # Check for factors of the form 6k ± 1
            return False
        i += 6
    return True

# Test the function
if is_prime(6):
    print("6 is prime")
else:
    print("6 is not prime")

if is_prime(101):
    print("101 is prime")
else:
    print("101 is not prime")

if is_prime(11):
    print("11 is prime")
else:
    print("11 is not prime")

if is_prime(13441):
    print("13441 is prime")
else:
    print("13441 is not prime")

if is_prime(61):
    print("61 is prime")
else:
    print("61 is not prime")

if is_prime(4):
    print("4 is prime")
else:
    print("4 is not prime")

if is_prime(1):
    print("1 is prime")
else:
    print("1 is not prime")
```

This script contains a function `is_prime(n)` that checks whether a given number `n` is prime or not. It first checks for basic conditions such as `n` being less than or equal to 1, and then checks for divisibility by 2 and 3. If `n` is divisible by either of these numbers, it's not prime. Otherwise, it checks for factors of the form `6k ± 1` up to the square root of `n` and returns `False` if it finds any. If it doesn't find any factors, it returns `True`, indicating that `n` is prime. The script then tests the function with the provided example numbers.