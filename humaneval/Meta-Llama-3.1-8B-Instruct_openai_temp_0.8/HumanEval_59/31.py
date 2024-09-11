### Largest Prime Factor
#### Problem Description
This script solves the problem of finding the largest prime factor of a given number.

#### Code
```python
def largest_prime_factor(n: int):
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

# Test the function
print(largest_prime_factor(13195))  # Expected output: 29
print(largest_prime_factor(2048))   # Expected output: 2
```

#### Explanation
This script uses a while loop to find the largest prime factor of the input number `n`. It starts by checking if `n` is divisible by `i`, where `i` is a number starting from 2. If `n` is divisible by `i`, it divides `n` by `i` and continues the loop. If `n` is not divisible by `i`, it increments `i` by 1 and continues the loop until `i` squared is less than or equal to `n`. At this point, `n` is the largest prime factor of the original input number.