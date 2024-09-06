```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Check for edge cases: 2 and 5
    if n == 2 or n == 5:
        return n
    # Divide n by 2, 3, 5, 7, 11, ...
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            n //= i
    # If n is still greater than 1, it is a prime
    if n > 1:
        return n
    # Otherwise, n must be 1
    return 1
```

This algorithm first checks if the number is 2, 5, or 1 and returns accordingly. If neither of these is the case, it iterates through potential divisors in an optimized way, dividing by 2, 3, 5, 7, 11, ... (i.e., the prime numbers less than or equal to the square root of n). The while loop repeatedly divides n by the largest factor it finds in this process. Eventually, n will become 1, or a prime number greater than 1. The function returns n in either case. 

This algorithm is paradigms of efficient coding: it runs in linear time and uses constant space, benefiting from the optimization common to all programmers of using built-in functions (such as int(n**0.5) for calculating square roots) to increase readability and efficiency. 

Note that this function assumes that n is not prime and is greater than 1, as stated in the docstring. To handle other cases, you can use Python's built-in functions: for prime numbers, use the math.isprime() function; to find the largest factor for all numbers, you can use the max() function.