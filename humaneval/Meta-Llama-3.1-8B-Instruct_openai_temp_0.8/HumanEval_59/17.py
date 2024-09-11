## Largest Prime Factor Function
### Problem Description

The function `largest_prime_factor` computes the largest prime factor of a given integer `n`. This function assumes that `n` is greater than 1 and is not a prime number itself.

### Solution
```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n.
    
    Assume n > 1 and is not a prime.
    
    Parameters:
    n (int): The number to find the largest prime factor of.
    
    Returns:
    int: The largest prime factor of n.
    
    Example:
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def is_prime(num: int) -> bool:
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    max_factor = 1
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            n //= i
            if is_prime(i):
                max_factor = max(max_factor, i)
    if is_prime(n):
        max_factor = max(max_factor, n)
    return max_factor
```

### Explanation

This solution uses a helper function `is_prime` to check if a number is prime. The main function `largest_prime_factor` iterates from 2 to the square root of `n` and checks each number to see if it is a factor of `n`. If `n` is divisible by a number `i`, it divides `n` by `i` and checks if `i` is prime using the `is_prime` function. If `i` is prime, it updates the `max_factor` to the larger of the current `max_factor` and `i`. After the loop, if `n` is still greater than 1, it means that `n` itself is prime, so it updates `max_factor` to be the larger of `max_factor` and `n`. Finally, it returns the `max_factor`.