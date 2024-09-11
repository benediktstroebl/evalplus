### Largest Prime Factor
#### Problem Solution

Here's a Python script that implements the `largest_prime_factor` function:

```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
        n (int): The input number.

    Returns:
        int: The largest prime factor of n.
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


### Example Usage

if __name__ == "__main__":
    print(largest_prime_factor(13195))  # Output: 29
    print(largest_prime_factor(2048))   # Output: 2
```

This solution uses a simple trial division method to find the largest prime factor of `n`. It iterates from `2` to the square root of `n` (inclusive), and at each step, it checks if `n` is divisible by the current number `i`. If it is, `n` is divided by `i`, effectively removing the factor from `n`. This process continues until `n` is no longer divisible by any number `i` up to its square root. The remaining value of `n` is the largest prime factor.

Note that this solution assumes that `n > 1` and is not a prime number.