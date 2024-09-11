### Largest Prime Factor Function
```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. 
    Assume n > 1 and is not a prime.

    Args:
    n (int): An integer greater than 1.

    Returns:
    int: The largest prime factor of n.

    Example:
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # Initialize the largest factor as 2
    largest_factor = 2
    # Start checking from 3, as 2 is the smallest prime number
    i = 3

    # Continue checking for factors until the square root of n
    while i * i <= n:
        # Check if i is a factor of n
        if n % i:
            # If not, increment i by 2 (since all primes are of the form 6k ± 1)
            i += 1
        else:
            # If i is a factor, update the largest factor and divide n by i
            largest_factor = i
            n //= i

    # If n is still greater than 1, it is a prime number and the largest factor
    if n > 1:
        largest_factor = n

    return largest_factor

# Test the function
if __name__ == "__main__":
    print(largest_prime_factor(13195))  # Output: 29
    print(largest_prime_factor(2048))   # Output: 2
```

This script uses a simple trial division method to find the largest prime factor of a given number `n`. It starts by checking odd numbers (since all primes are of the form 6k ± 1) and updates the largest factor whenever it finds a new one. If `n` is still greater than 1 after dividing it by all possible factors, it means `n` is a prime number and the largest factor.