```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Loop through each number from 2 to the input number n.
    for i in range(2, n):
        # Check if n is divisible by i, and if i is prime. If both are true, return i.
        if n % i == 0 and is_prime(i):
            return i
    # If none of the above conditions are met, return n. This means n is a prime number.
    return n

def is_prime(n):
    """Return True if n is a prime number, False otherwise."""
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
```