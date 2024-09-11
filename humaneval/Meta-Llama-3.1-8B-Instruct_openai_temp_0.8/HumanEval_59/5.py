### Largest Prime Factor
#### Problem Description
Find the largest prime factor of a given number `n`.

#### Solution

```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
        n (int): Input number.

    Returns:
        int: Largest prime factor of n.

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
```

#### Explanation
This script uses a simple trial division method to find the largest prime factor of a given number `n`.

1. We start with `i = 2` and check if `n` is divisible by `i`.
2. If `n` is not divisible by `i`, we increment `i` by 1.
3. If `n` is divisible by `i`, we divide `n` by `i` (integer division) and repeat the process with the new value of `n`.
4. We continue this process until `i * i > n`, at which point `n` must be a prime number and is the largest prime factor of the original `n`.

#### Example Use Cases
```python
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```