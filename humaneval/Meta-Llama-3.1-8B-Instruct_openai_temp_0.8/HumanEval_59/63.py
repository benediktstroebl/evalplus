```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    :param n: The input number
    :return: The largest prime factor of n
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

This script uses a simple trial division method to find the largest prime factor of a given number. The `while` loop runs until `i` squared is greater than `n`, and in each iteration, it checks if `n` is divisible by `i`. If it is, `n` is divided by `i` to reduce the problem size. The loop continues until `i` squared is greater than `n`, at which point the remaining `n` is the largest prime factor.