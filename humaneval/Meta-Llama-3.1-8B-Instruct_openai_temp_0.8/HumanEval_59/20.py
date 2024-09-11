### Largest Prime Factor Function
```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.
    Assume n > 1 and is not a prime.

    Args:
        n (int): The input number.

    Returns:
        int: The largest prime factor of n.

    Examples:
        >>> largest_prime_factor(13195)
        29
        >>> largest_prime_factor(2048)
        2
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


# Test cases
if __name__ == "__main__":
    print(largest_prime_factor(13195))  # Output: 29
    print(largest_prime_factor(2048))   # Output: 2
```
This script uses a while loop to iterate from 2 to the square root of `n` (inclusive), and checks each number to see if it's a factor of `n`. If it is, it divides `n` by that factor. This process continues until `n` is no longer divisible by any number up to its square root. At this point, `n` is the largest prime factor of itself, so the function returns it.