### Largest Prime Factor Function
```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
        n (int): A number greater than 1 that is not a prime.

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

# Test the function
if __name__ == "__main__":
    print(largest_prime_factor(13195))  # Output: 29
    print(largest_prime_factor(2048))   # Output: 2
```
This script defines a function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. It uses a while loop to divide `n` by the smallest divisor `i` starting from 2, until `n` is no longer divisible by `i`. The largest prime factor is then returned as the remaining value of `n`. The script also includes test cases to demonstrate the function's correctness.