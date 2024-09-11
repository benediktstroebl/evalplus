```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    :param n: The input number.
    :return: The largest prime factor of n.
    """
    i = 2
    while n > 1:
        if n % i == 0:
            n = n // i
        else:
            i += 1
    return n


# Test cases
print(largest_prime_factor(13195))  # Expected output: 29
print(largest_prime_factor(2048))   # Expected output: 2
```

This script defines the `largest_prime_factor` function, which finds the largest prime factor of a given number `n`. It uses a while loop to continuously divide `n` by the smallest divisor (`i`) until `n` is reduced to 1. The largest prime factor is then returned. The script includes two test cases to demonstrate the function's correctness.