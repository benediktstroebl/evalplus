### Largest Prime Factor Function
#### Problem Statement
The following Python function calculates the largest prime factor of a given number `n`. It assumes that `n` is a composite number (not prime) and greater than 1.

#### Code
```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
    n (int): A composite number greater than 1.

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
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```
#### Explanation
This function works by dividing the input number `n` by the smallest prime factor `i` as long as it's divisible. The process continues until `n` is no longer divisible by `i`. The last value of `n` before the loop ends is the largest prime factor of the original number.