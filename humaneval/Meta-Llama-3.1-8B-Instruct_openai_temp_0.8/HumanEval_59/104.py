```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.

    Assume n > 1 and is not a prime.

    :param n: Input number
    :return: Largest prime factor of n
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

This script finds the largest prime factor of a given number `n`. It uses a while loop to divide `n` by the smallest divisor `i` until `n` is no longer divisible by `i`. Since `i` starts from 2 (the smallest prime number), `n` will only have prime numbers as its divisors at this point. The loop continues until `i` is greater than the square root of `n`, because any factor larger than the square root would have a corresponding factor smaller than the square root.