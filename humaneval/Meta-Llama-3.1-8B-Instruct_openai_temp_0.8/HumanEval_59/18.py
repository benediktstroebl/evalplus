```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n.
    
    Assume n > 1 and is not a prime.
    
    :param n: An integer greater than 1
    :return: The largest prime factor of n
    
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
print(largest_prime_factor(13195))  # 29
print(largest_prime_factor(2048))   # 2
```

This script defines a function called `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. It works by dividing `n` by the smallest prime factor it can find, which is `2`, and repeating this process until `n` is no longer divisible by `2`. It then increments the divisor and checks if it's a factor of `n`. This process continues until `n` is reduced to its largest prime factor, which is then returned.

The time complexity of this function is O(sqrt(n)) because the loop runs until the square root of `n` is reached. The space complexity is O(1) as it uses a constant amount of space.