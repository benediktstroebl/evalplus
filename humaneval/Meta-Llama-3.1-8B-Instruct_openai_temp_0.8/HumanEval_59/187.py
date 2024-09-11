### Largest Prime Factor Function
#### Python Code

```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
    n (int): A composite integer greater than 1.

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

# Example usage
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

### Explanation

This function takes an integer `n` as input, which is assumed to be a composite number (not a prime). It iteratively divides `n` by the smallest divisor `i` starting from 2. Since the number is composite, `n` will have some divisor less than or equal to its square root. Thus, the while loop checks all possible divisors up to the square root of `n`.

If `n` is divisible by `i`, it is divided by `i`. This process continues until `n` is no longer divisible by `i`. At that point, `i` is incremented until it finds the next divisor or surpasses the square root of `n`.

Once the loop completes, `n` will be the largest prime factor of the original input. This is because any remaining divisors that are greater than the square root of `n` have already been eliminated in the loop.