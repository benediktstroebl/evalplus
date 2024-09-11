```python
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.

    :param n: The input number
    :return: The largest prime factor of n
    """
    # Start from 2 and check if it's a factor
    i = 2
    while i * i <= n:
        # If i is a factor, find the largest prime factor
        if n % i:
            # If i is not a factor, increment it by 1
            i += 1
        else:
            # If i is a factor, divide n by i
            n //= i
    # At the end, n is the largest prime factor
    return n

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```
This script works by dividing the input number `n` by the smallest prime factor (which is 2) as long as it's divisible. Then it increments the divisor by 1 and continues the process. Since we're checking divisibility up to the square root of `n`, we can stop once the divisor exceeds the square root. At the end, `n` will be the largest prime factor.