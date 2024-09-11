```python
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            return i
    return 1

# Test cases
print(largest_divisor(15))  # Expected output: 5
print(largest_divisor(20))  # Expected output: 10
print(largest_divisor(13))  # Expected output: 1
```

This script iterates from `n-1` downwards to find the largest number that divides `n` evenly. It uses the modulo operator (`%`) to check for divisibility. If a divisor is found, it is immediately returned. If no divisors are found (i.e., the number is prime), the function returns 1, since 1 is the only divisor of a prime number besides the number itself.