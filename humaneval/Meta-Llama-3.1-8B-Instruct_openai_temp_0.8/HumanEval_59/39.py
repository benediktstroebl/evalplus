```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n.
    Assume n > 1 and is not a prime.

    :param n: An integer greater than 1
    :return: The largest prime factor of n
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

# Example usage:
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```
This script defines the function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. It uses a simple trial division method to find the largest prime factor. The loop starts from 2 and checks divisibility of `n` by increasing integers. If `n` is divisible by an integer `i`, it updates `n` to be the quotient of `n` and `i`, effectively dividing `n` by `i`. The loop continues until `i` is greater than the square root of `n`, at which point `n` itself is the largest prime factor.