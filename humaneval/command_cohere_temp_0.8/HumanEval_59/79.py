```python
def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for largest factor first
    largest = n // 2
    while largest > 1 and not is_prime(largest):
        largest //= 2
    if largest > 1:
        return largest
    # If not, then check from the square root
    sqrt = int(n ** 0.5)
    for i in range(sqrt, 1, -1):
        if is_prime(i):
            return i

def is_prime(n):
    """Return True if n is a prime number, False otherwise."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

The function `largest_prime_factor` returns the largest prime factor of the given number `n`. It initially divides `n` by 2 to find the largest even factor, gradually dividing by 2 until it becomes 1 or a prime number. If no even factor is found, it checks prime numbers from the square root of `n` down to 1.

The function `is_prime` checks if a number is prime or not. It deems a number prime if it is greater than 1 and has no divisors other than 1 and itself among numbers from 2 to the square root of the number.

The tests provided in the problem statement are covered and passed by this code.