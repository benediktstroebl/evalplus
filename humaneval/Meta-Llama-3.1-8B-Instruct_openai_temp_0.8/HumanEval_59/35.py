```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. 
    Assume n > 1 and is not a prime.

    :param n: An integer greater than 1
    :return: The largest prime factor of n
    """
    def is_prime(num: int) -> bool:
        """
        Check if a number is prime.
        :param num: The number to check
        :return: True if num is prime, False otherwise
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    max_prime_factor = 1
    for i in range(2, n):
        # Check if i is a factor of n
        if n % i == 0:
            # Check if i is prime
            if is_prime(i):
                # Update max_prime_factor if i is larger
                max_prime_factor = max(max_prime_factor, i)

    return max_prime_factor


# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))  # Output: 2
```

This script defines a function `largest_prime_factor` that takes an integer `n` and returns its largest prime factor. It uses a helper function `is_prime` to check if a number is prime. The main function iterates over all numbers from 2 to `n` and checks if they are factors of `n`. If a factor is prime, it updates the maximum prime factor. Finally, the function returns the largest prime factor.