```markdown
### Largest Prime Factor
#### Problem Description
Find the largest prime factor of a given number `n`.

#### Solution
```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
    n (int): A number greater than 1, not a prime.

    Returns:
    int: The largest prime factor of n.

    Example:
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Initialize the largest factor
    largest_factor = 2

    # Check from 3 to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            # If i is a factor, update the largest factor and divide n by i
            largest_factor = max(largest_factor, i)
            n //= i

    # If n is still greater than 2, it means n is a prime number
    if n > 2:
        # Return n as it is the largest prime factor
        return n
    else:
        # Return the largest factor found
        return largest_factor

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script uses a simple trial division method to find the largest prime factor of a given number `n`. It starts by dividing `n` by 2, then checks odd numbers up to the square root of `n` to find its factors. If `n` is still greater than 2 after the loop, it means `n` is a prime number and is returned as the largest prime factor.