```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.
    Assume n > 1 and is not a prime.
    
    :param n: An integer greater than 1.
    :return: The largest prime factor of n.
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script uses a while loop to find the largest prime factor of a given number. It starts from 2, the smallest prime number, and checks if the given number is divisible by the current number. If it is, it divides the number by the current number. If it's not, it increments the current number. This process continues until the number is reduced to 1. The number that was used for the last division is the largest prime factor of the original number.