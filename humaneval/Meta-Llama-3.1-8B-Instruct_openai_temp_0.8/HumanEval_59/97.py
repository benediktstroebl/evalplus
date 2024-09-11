```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    :param n: A positive integer greater than 1.
    :return: The largest prime factor of n.
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

This script uses a simple trial division method to find the largest prime factor of a given number. It starts by checking divisibility from 2, then increments the divisor by 1 each time. When it finds a divisor, it removes that divisor from the original number and continues the search. Since a larger divisor is guaranteed to be a multiple of the previous divisor, the inner loop can stop once the square root of the number is reached, making it more efficient than a naive approach that checks all numbers up to the number itself.