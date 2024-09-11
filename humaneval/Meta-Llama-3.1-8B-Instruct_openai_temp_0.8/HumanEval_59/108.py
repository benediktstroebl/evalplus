```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n.
    
    Args:
    n (int): A number greater than 1 and not a prime.

    Returns:
    int: The largest prime factor of n.

    Example:
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
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

In this script, we define a function `largest_prime_factor(n)` that takes an integer `n` as input. We then enter a while loop where we continuously divide `n` by the smallest divisor `i` until `n` is no longer divisible by `i`. We keep track of the current value of `n` as we iterate, so once `n` is no longer divisible by `i`, we return `n` as it will be the largest prime factor of the original `n`. 

We test the function with the provided example inputs.