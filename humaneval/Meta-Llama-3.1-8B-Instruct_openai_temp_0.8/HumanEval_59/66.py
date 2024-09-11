```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
        n (int): The input number.

    Returns:
        int: The largest prime factor of n.
    """
    def is_prime(num: int) -> bool:
        """
        Helper function to check if a number is prime.

        Args:
            num (int): The number to check.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    largest_factor = 1
    for i in range(2, n + 1):
        # Check if i is a factor of n
        if n % i == 0:
            # Check if i is a prime number
            if is_prime(i):
                largest_factor = max(largest_factor, i)

    return largest_factor

# Test cases
print(largest_prime_factor(13195))  # 29
print(largest_prime_factor(2048))   # 2
```